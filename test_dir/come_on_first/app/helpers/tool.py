# encoding:utf-8
import config
from flask import Response, json
from datetime import datetime, date, time
from decimal import Decimal


class APIEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(o, date):
            return o.strftime("%Y-%m-%d")
        elif isinstance(o, time):
            return o.isoformat()
        elif isinstance(o, Decimal):
            return float(o)
        print type(o)
        return json.JSONEncoder.default(self, o)


def get_result(status, data):
    return {'code': config.errcode.get(status),
            'result': data,
            'errmsg': config.errmsg.get(status)}


def jsonify(data):
    return Response(json.dumps(data, cls=APIEncoder), mimetype='application/json')


def class_to_dict(obj):
    dic = {}
    dic.update(obj.__dict__)
    if "_sa_instance_state" in dic:
        print dic['_sa_instance_state']
        del dic['_sa_instance_state']
    return dic


