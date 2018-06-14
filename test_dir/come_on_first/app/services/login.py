# encoding: utf-8

from app.models.users import Users
from app.helpers.tool import *
from datetime import timedelta
from config import config
from app.helpers.build_redis import check_token


@check_token
def get_user(telephone, password):
    login_user = Users.query.filter(Users.telephone == telephone).first()
    if not login_user:
        return {"ERROR": "WRONG_PASSWORD"}
    if login_user.password == password:
        expire_time = datetime.now() + timedelta(seconds=config.get("APP_LOGIN_EXPIRE"))
        data = {
            "id": login_user.id,
            "telephone": telephone,
            "username": login_user.username,
            "create_time": login_user.create_time,
            "expire_time": expire_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        return {"DATA": data}
    else:
        return {"ERROR": "WRONG_PASSWORD"}
