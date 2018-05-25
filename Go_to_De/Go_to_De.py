# encoding: utf-8

from flask import Flask, url_for, redirect, render_template
import config
# 初始化一个flake对象  Flask()
# 需要传递一个参数 __name__
# 方便flask框架去寻找资源，方便flask插件，出现错误的时候寻找问题所在位置
app = Flask(__name__)
app.config.from_object(config)
# @app.route 是一个装饰器
# 这个装饰器的作用是 一个url与视图函数的映射
# 请求函数，并返回结果给浏览器


@app.route('/')
def hello_world():
    # 模板传参方式
    context = {
        "username": "liyu",
        "gender": "man",
        "age": 18
    }
    # login_url = url_for('login')
    # print url_for('article', id="test")
    # 作用，在url地址发生变化，而视图函数名称未变化时，依然能够正常访问
    # return redirect(login_url)
    # return "hello world!"
    return render_template("index.html", context=context)


@app.route('/user_info/<is_login>/')
def user_info(is_login):
    # 模板中if语句使用，模板传参方式
    user = {
        "name": "liyu",
        "age": 17
    }
    if is_login == "1":
        return render_template("user_info.html", user=user)
    else:
        return render_template("user_info.html")


@app.route('/article/<id>')
def article(id):
    # 在url中使用变量
    return u"请求ID是：%s "% id


@app.route('/login/')
def login():
    # 模板中传参方式
    user = {
        "username": "liyu",
        "gender": "man",
        "age": 18
    }
    return render_template("login.html", **user)


@app.route('/question/<is_login>')
def question(is_login):
    # 重定向以及url反转
    if is_login == '1':
        return u'这是问答页面'
    else:
        return redirect(url_for('login'))


@app.route('/forstate')
def forstate():
    user = {
        "username": "liyu",
        "gender": "man",
        "age": 18
    }
    websites = ['baidu.com', 'google.com']
    return render_template('forstate.html', user=user, websites=websites)


@app.route('/comments')
def comments():
    return render_template('comments.html')


if __name__ == '__main__':
    # 如果当前这个文件是作为入口程序运行，那么就执行app.run()
    # 启动一个应用服务器来接收用户请求
    # while True：     # 一个死循环，持续监听
    #   listen()
    app.run()
