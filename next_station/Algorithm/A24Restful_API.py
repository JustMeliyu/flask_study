# encoding: utf-8
"""
理解 RESTful 框架
http://www.ruanyifeng.com/blog/2011/09/restful.html
RESTful API 设计指南
http://www.ruanyifeng.com/blog/2014/05/restful_api.html
https://www.cnblogs.com/jonathan1314/p/7154243.html

    1: REST 是 Representation State Transfer 的简写, 译为 表现层状态转化;
        如果一个架构符合REST原则, 就称为RESTful 架构
    2: 资源(Resources)
        REST中缺少主语, 表现层其实是指 "资源" 的表现层;
        资源 就是指网络中的一个实体, 或则说是网络上的一个具体信息. 比如一张图片, 一段文本等;
        可以用一个URI(统一资源定位符)指向它, 每种资源对应一个URI, 使用URI来对这些资源进行唯一访问
    3: 表现层(Representation)
        资源 是一种信息实体, 它可以有多种表现形式. 我们把 资源 表现出来的形式, 叫做 "表现层";
        比如文本可以用 txt格式表现, 也可以用HTML, XML等格式表现;
        URI 只代表资源的实体, 及其"资源"的位置, 不代表形式;
        具体表现形式应该在HTTP请求的头信息中用Accept和Content-Type字段指定.
    4: 状态转化(State Transfer)
        访问一个网站, 代表了客户端与服务器之间的交互, 所有的状态都保存在服务器端.
        如果客户端想要操作服务器, 必须通过某种手段, 让服务器端发生 "状态转化". 这种转化是建立在表现层之上的, 所以就是"表现层状态转化"
        客户端用到的手段,只能是HTTP协议.具体来说,就是HTTP协议里面,四个表示操作方式的动词：GET、POST、PUT、DELETE;
        它们分别对应四种基本操作：GET用来获取资源,POST用来新建资源（也可以用于更新资源）,PUT用来更新资源,DELETE用来删除资源.
    5: 综述 RESTful架构:
        1: 每个URI代表一种资源;
        2: 客户端与服务器之间, 传递这种资源的某种表现层;
        3: 客户端通过四个HTTP动词, 对服务器端资源进行操作, 实现 "表现层状态转化"
    6: 误区
    RESTful架构有一些典型的设计误区
        1: 最常见的一种设计错误,就是URI包含动词
        因为"资源"表示一种实体,所以应该是名词,URI不应该有动词,动词应该放在HTTP协议中.
        2: 另一个设计误区,就是在URI中加入版本号
        因为不同的版本,可以理解成同一种资源的不同表现形式,所以应该采用同一个URI.版本号可以在HTTP请求头信息的Accept字段中进行区分
    服务器返回的数据格式,应该尽量使用JSON,避免使用XML
    7: 通俗语言解释REST和RESTful API
    URL定位资源,用HTTP动词(GET,POST,PUT,DELETE)描述操作
        1: REST描述的是网络中clien和server的一种交互形式;REST本身不实用,实用的是如何设计RESTful API(REST风格的网络接口)
        2: Server提供的RESTful API中,URL只使用名词来指定资源,原则上不使用动词.“资源”是REST架构或者说整个网络处理的核心
        3: 用HTTP协议里的动词来实现资源的获取,添加,修改和删除等操作
        4: Server 和 Client之间传递某种资源的一个表现形式.如json、xml传输文本,png、jpg传输图片等
        5: 用 HTTP Status Code 传递Server的状态信息

    传统的接口设计, 就是过程式的, 每个特定的动作有特定的接口.
    RESTful, 其实就是一个面向对象的接口, 接口是对象, 这个对象有GET, POST, PUT, DELETE等等成员函数(接口)
"""
