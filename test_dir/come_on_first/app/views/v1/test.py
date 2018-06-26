# encoding: utf-8

import os
from flask import Blueprint, request, json
from config import data as c_data
from app.helpers.tool import *
from datetime import datetime
g_test = Blueprint("g_test", __name__)


@g_test.route("/read_txt_file")
def read_txt_file():
    # t_file = request.files.get("file")
    # token = request.values.get("token")
    f_path = os.path.join(c_data.file_path.get("read"), "tag.txt")
    try:
        os.mkdir(c_data.file_path.get("read"))
    except OSError:
        pass
    try:
        f_name = open(f_path, "w")
    except IOError:
        return jsonify(get_result("NO_FILE", {}))
    f_name.write("sss\n")
    f_name = open(f_path, "r")
    st = f_name.read()
    f_name.close()
    return jsonify(get_result("SUCCESS", {"string": st}))


@g_test.route("/read_json_file", methods=["POST"])
def read_json_file():
    j_file = request.files.get("file")
    if j_file is None:
        return jsonify(get_result("NO_FILE", {}))
    f_name = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S") + j_file.filename
    f_path = os.path.join(c_data.file_path.get("read"), f_name)
    j_file.save(f_path)
    fp = open(f_path, "a+")
    j_content = json.load(fp)
    r_dic = {}
    for k, v in j_content.items():
        print "{} : {}".format(k, v)
        r_dic[k] = v
    print(type(fp))
    return jsonify(get_result("SUCCESS", j_content))


@g_test.route("/post_json", methods=["POST"])
def post_json():
    # title = request.get_json(silent=True).get("title")
    title = get_data("title")
    content = get_data("content")
    # content = request.get_json(silent=True).get("content")

    data = {
        "title": title,
        "content": content
    }

    return jsonify(get_result("SUCCESS", data))
