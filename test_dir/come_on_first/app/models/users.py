# encoding:utf-8
from config import db
from datetime import datetime


class Users(db.Model):
    """用户表"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    create_time = db.Column(db.DateTime)
    permissions = db.Column(db.Integer, nullable=False)

    def __init__(self, telephone, username, password, permissions, create_time=None):
        self.telephone = telephone
        self.username = username
        self.password = password
        self.permissions = permissions
        self.create_time = create_time if create_time else datetime.now()
