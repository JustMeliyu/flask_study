# -*-coding:utf-8-*-
import sys
import json
import xlrd
SQ_USER = {
        "上海": "999020", "浙江": "999031", "江苏": "999021", "安徽": "999023", "江西": "999033", "福建": "999035",
        "北京": "999010", "天津": "999030", "河北": "999050", "山西": "999034", "内蒙古": "999012", "广东": "999051",
        "香港": "999852", "海南": "999057", "广西": "999053", "湖北": "999043", "河南": "999045", "湖南": "999041",
        "山东": "999025", "辽宁": "999011", "黑龙江": "999015", "吉林": "999013", "陕西": "999071", "青海": "999081",
        "甘肃": "999073", "宁夏": "999075", "新疆": "999083", "重庆": "999040", "四川": "999061", "云南": "999065",
        "贵州": "999055", "西藏": "999085", "台湾": "999886", "澳门": "999853"
    }


def init_data():
    a = {}
    for k, c in SQ_USER.items():
        a[c] = {"codes": [], 'province': k}
    return a


def write_json_file(file_path, data):
    with open(file_path, 'w') as load_f:
        json.dump(data, load_f, ensure_ascii=False)


def get_code(addr):
    wb = xlrd.open_workbook(addr)
    ws = wb.sheet_by_name("Sheet1")

    codes = ws.col_values(1, 1)
    provinces = ws.col_values(3, 1)
    province_location_codes = init_data()
    a = []
    for i in range(len(provinces)):
        p_code = SQ_USER.get(provinces[i].encode('utf-8'))
        if not p_code:
            print("++", provinces[i])
            continue
        code = str(int(codes[i])).zfill(6)
        if code not in province_location_codes[p_code]['codes']:
            province_location_codes[p_code]['codes'].append(code)
        else:
            print("--", code)
            a.append(code)
    write_json_file("./tmp.json", province_location_codes)


if __name__ == "__main__":
    get_code("/home/ly/province_locaion_20190418.xlsx")
