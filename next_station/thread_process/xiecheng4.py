# -*-coding:utf-8-*-
import xlwt
import xlrd
import time
import inspect
import os
from collections import Iterable


def write_rows(worksheet: xlwt.Worksheet):
    print('Start to process write_rows in %s' % worksheet.name)
    row_index = 0
    while True:
        row = yield
        if row is None:
            break
        for col_index, cell in enumerate(row):
            worksheet.write(row_index, col_index, cell.value)
        row_index += 1
    print('Complete writing %d rows in %s' % (row_index, worksheet.name))


def write_sheets(workbook: xlwt.Workbook, sheet_names: Iterable):
    for sheet_name in sheet_names:
        print('Start to process %s' % sheet_name)
        sheet = workbook.add_sheet(sheet_name)
        yield from write_rows(sheet)
        print('Sheet %s is done' % sheet_name)


def write_book(dst_path: str, book_name: str, sheet_names: Iterable):
    print('Start to process %s' % book_name)
    book = xlwt.Workbook(encoding='gb2312')
    yield from write_sheets(book, sheet_names)
    book.save(os.path.join(dst_path, r'%s.xls') % book_name)
    print('File %s.xls is saved' % book_name)
    yield


def build_generators(dst_path: str, partition_values: Iterable, sheet_names: Iterable) -> dict:
    partition_values = list(partition_values)
    sheet_names = list(sheet_names)
    workbooks = {partition_value: write_book(dst_path, partition_value, sheet_names) for partition_value in partition_values}
    return workbooks


def read_src_workbook(src_path: str, dst_path: str, partition_key: str, partition_values: Iterable):
    with xlrd.open_workbook(src_path) as xlsfile:
        time_stamp = time.time()
        sheet_names = xlsfile.sheet_names()
        workbooks = build_generators(dst_path, partition_values, sheet_names)
        # 预激生成器
        for partition_value, generator in workbooks.items():
            next(generator)
            print('The status of generator {0} is {1}'.format(partition_value, inspect.getgeneratorstate(generator)))

        for src_sheet in xlsfile.sheets():
            key_index = src_sheet.row_values(0).index(partition_key)
            for src_row in src_sheet.get_rows():
                this_partition_value = src_row[key_index].value
                if this_partition_value in workbooks:
                    workbooks[src_row[key_index].value].send(src_row)
            # 结束子生成器
            for generator in workbooks.values():
                generator.send(None)
        # 结束派生生成器
        for generator in workbooks.values():
            try:
                next(generator)
            except StopIteration:
                pass
        print('Totally use %.1fs' % (time.time() - time_stamp))


if __name__ == "__main__":
    read_src_workbook("/home/ly/code/my_project/training/training/test.xlsx", "./", "1", [1, 3, 4])
