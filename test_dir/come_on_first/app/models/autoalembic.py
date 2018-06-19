# encoding: utf-8

from config import db


class Autoalembic(db.Model):
    __tablename__ = 'autoalembic'
    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

