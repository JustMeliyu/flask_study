# -*-coding:utf-8-*-
import json
import datetime


class APIEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, datetime.time):
            return obj.isoformat()
        '''
        elif isinstance(obj,ObjectId):
            return str(obj)
        '''
        return json.JSONEncoder.default(self, obj)
