# encoding:utf-8
import config
from flask import Response, json, request
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
        del dic['_sa_instance_state']
    return dic


def get_data(param):
    if request.method in ["POST", "PUT"]:
        if hasattr(request, "json") and request.json:
            return request.get_json(silent=True).get(param)
    return request.values.get(param)
