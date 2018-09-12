# encoding:utf-8
# 引入模块
from flask_wtf import FlaskForm, CsrfProtect
# 如果输入的是字符串就用StringField, 数字就用IntegerField
from wtforms import StringField, IntegerField
# 验证方式
from wtforms.validators import Length, EqualTo, InputRequired


class RegistForm(FlaskForm):
    username = StringField(validators=[Length(min=3, max=10, message=u'用户名长度错误')])
    password = StringField(validators=[Length(min=6, max=20)])
    # age = IntegerField(validators=[InputRequired])
