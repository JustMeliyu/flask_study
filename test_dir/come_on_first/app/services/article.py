# encoding: utf-8

import xlrd
from app.models.articles import Articles
from app.models.users import Users
from app.helpers.public import class_to_dict
from app.helpers.build_redis import is_login
import traceback
from config import logger, db, data as c_data
# from config import data as c_data
from flask import g
from datetime import datetime


def get_page_article(page_index, page_size, sort, title, content, article_type):
    try:
        query_result = Articles.query
        if sort:
            query_result = query_result.order_by(db.desc(Articles.create_time))
        if title:
            query_result = query_result.filter(Articles.title.like('%{}%'.format(title)))
        if content:
            query_result = query_result.filter(Articles.content.like('%{}%'.format(content)))
        if article_type:
            query_result = query_result.filter(Articles.type.like('%{}%'.format(article_type)))
        paginate = query_result.paginate(page_index, page_size, False)
        data = {
            "total": len(paginate.items),
            "data": [class_to_dict(item) for item in paginate.items]
        }
        return {"DATA": data}
    except:
        db.session.rollback()
        logger.info(traceback.format_exc())
        return {"ERROR": "DB_ERROR"}


@is_login
def p_article(title, content, article_type):
    if article_type not in c_data.article_type:
        return {"ERROR": "PARAM_ERROR"}
    if len(title) > 30:
        return {"ERROR": "PARAM_ERROR"}
    try:
        article = Articles(title=title, content=content, type=article_type, author_id=g.current_user_id)
        db.session.add(article)
        db.session.commit()
        data = {
            "id": article.id,
            "title": title,
            "content": content,
            "type": article_type,
            "author_id": g.current_user_id,
            "create_time": article.create_time
        }
        return {"DATA": data}
    except:
        db.session.rollback()
        logger.debug(traceback.format_exc())
        return {"ERROR": "DB_ERROR"}


def file_is_legal(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in c_data.file_legality


@is_login
def get_excel_data(file_path):

    all_article = get_data(file_path)
    # noinspection PyBroadException
    # try:
    #     for art in all_article:
    #         user = Users.query.filter_by(username=art.get('author')).first()
    #         if not user:
    #             return {"ERROR": "AUTHOR_NOT_EXIST"}
    #         article_ditail = Articles(title=art.get('title'),
    #                                   content=art.get('content'),
    #                                   type=art.get('type'),
    #                                   create_time=art.get('create_time'), author=user)
    #         db.session.add(article_ditail)
    #     db.session.commit()
    # except Exception:
    #     db.session.rollback()
    #     logger.info(traceback.format_exc())
    #     return {"ERROR": "DB_ERROR"}

    data = {
        "total": len(all_article),
        "data": all_article
    }
    return {"DATA": data}


def get_data(path):
    all_article = []
    merged = False
    # 获取excel中的数据
    excel_file = xlrd.open_workbook(path)
    file_sheet = excel_file.sheet_by_index(0)

    # 获取对应key值
    article_key = file_sheet.row_values(c_data.start_row - 2, end_colx=c_data.end_col)
    if article_key != c_data.article_key:
        return {"ERROR": "ERROR_FILE_CONTENT"}
    # 从start_row 开始读取数据， 抛开合并单元格部分
    for r in range(c_data.start_row - 1, file_sheet.nrows):
        # 判断创造时间格式
        if file_sheet.cell(r, c_data.end_col - 1).ctype != 3:
            return {"ERROR": "ERROR_FILE_CONTENT"}

        for (rlow, rhigh, clow, chigh) in file_sheet.merged_cells:
            if r == rlow:
                merged = True
                c_row = rlow
                break
            if r == rhigh:
                merged = False
                break
        author = file_sheet.cell_value(c_row, 0) if merged else file_sheet.cell_value(r, 0)
        article_value = file_sheet.row_values(r, start_colx=c_data.start_col - 1, end_colx=c_data.end_col)
        article_value.insert(0, author)
        # 改变存入日期格式
        article_value[c_data.end_col - 1] = xlrd.xldate_as_tuple(article_value[c_data.end_col - 1],
                                                                 excel_file.datemode)
        article_value[c_data.end_col - 1] = datetime(*article_value[c_data.end_col - 1][:6])
        article = dict(zip(article_key, article_value))
        all_article.append(article)
    return all_article
