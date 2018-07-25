# encoding: utf-8
import os
from flask import Blueprint, request, json, session, redirect
from config import db, data as c_data
from app.helpers.tool import *
from app.helpers.pagination import paginate
from datetime import datetime
from app.models.articles import Articles
from app.models.users import Users
from sqlalchemy import func, or_, and_

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


@g_test.route("/g_t")
def g_t():
    # Articles = app.models.articles.Articles
    # print(Articles)
    # print(type(Articles))
    articles = db.session.query(Articles.title).filter_by(id=1)
    print(articles)
    print("=======")
    # article = Articles.query.filter_by(type="movie").all()
    # print article.author
    # print article._class
    u = Users.query.filter_by(id=1).first()
    print u
    print u.articles
    print u.articles.all()
    return "hello"


@g_test.route("/g_p_a")
def g_p_a():
    title = request.values.get("title")
    content = request.values.get("content")
    type = request.values.get("type")
    author_id = 1
    try:
        article = Articles.new(title, content, type, author_id)
    except:
        print(1)
    return "ok"


# flask 各查询语句用法
@g_test.route("/r_query")
def r_query():

    author_id = 1
    # group_by 和 order_by 的用法
    result = db.session.query(Articles.author_id, func.count(author_id).label("num")).\
        group_by(Articles.author_id).order_by("num")
    r = paginate(result, 1, 10, error_out=False)
    print(r)
    print(r.total)
    print(r.items)
    print(result.all())

    # distinct
    r2 = db.session.query(Articles.author_id).distinct(Articles.author_id).all()
    print(r2)
    # __repr__
    print("========")
    r3 = Articles.query.filter_by(author_id=1).first()
    print(r3)
    print("========")
    # and or
    r4 = Articles.query.filter(or_(Articles.id == 1, Articles.id == 2))
    r5 = Articles.query.filter(and_(Articles.id == 1, Articles.author_id == 1))
    print r4
    print r5
    print("========")
    # not equals, like, ILKIE, MATCH
    """
    LIKE 用%代表任意字符，matches 使用*
    LIKE 用_代表一个字符，matches 使用？
    另外，matches 支持表达式匹配，如： field1 matches 'abc[123]'表示栏位匹配字母abc开头的第四位是1或2或3的资料。 
    """
    r1 = Articles.query.filter(Articles.title.match("thon"))
    r6 = Articles.query.filter(Articles.author_id != 1)
    r7 = Articles.query.filter(Articles.title.like("%{}%".format("python")))
    r8 = Articles.query.filter(Articles.title.ilike("%{}%".format("Python")))
    print(r1)
    print(r6)
    print(r7)
    print(r8)
    # IN , NOT IN, IS NULL , IS NOT NULL
    print("========")
    r9 = Articles.query.filter(Articles.type.in_(['movie', 'game']))
    r10 = Articles.query.filter(~Articles.type.in_(['movie', 'game']))
    r11 = Articles.query.filter(Articles.type.is_(None))
    r12 = Articles.query.filter(Articles.type.isnot(None))
    print r9
    print r10
    print r11
    print r12
    return "ok"


@g_test.route("/sso")
def sso_login():
    pass
