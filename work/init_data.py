# -*-coding:utf-8-*-
from datetime import datetime, timedelta
from next_station.common import request_sys, get_func_time
from next_station.logger import logger
import gevent
import random
from gevent import monkey

monkey.patch_all()


@get_func_time
def inin_data_order():
    url = "http://172.16.7.47:5001/v1/orders/create/order"
    re_data = {
        "line_no": "MOT000004TO00000101",
        "carrier_code": "203",
        "antipate_arrive_time": (datetime.now() + timedelta(hours=5)),
        "demand_carriage_type": "XS",
        "order_demand": [{
            "carriage_length_type": u"6.8米",
            "vehicle_amount": 2
        }, {
            "carriage_length_type": u"7.6米",
            "vehicle_amount": 2
        }, {
            "carriage_length_type": u"9.6米",
            "vehicle_amount": 2
        }, {
            "carriage_length_type": u"14.5米",
            "vehicle_amount": 2
        }, {
            "carriage_length_type": u"17.5米",
            "vehicle_amount": 2
        }]
    }
    settlement_type = random.choice(['ZC', 'JZ'])
    re_data['settlement_type'] = settlement_type
    if settlement_type == "JZ":
        re_data['require_total_volume'] = random.randint(50, 300)
    else:
        re_data['require_total_volume'] = ""
    reqheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                  'Content-Type': 'application/json', 'token': "ST-1269-ghei4VdqVEb6yQZGsbti-cas01.example.org"}
    re = request_sys(url, re_data, "POST", reqheaders)
    if not re or re['code'] != 1000:
        logger.info("result is {0}".format(re))


def init_data_order_vehicles(order_number):
    plate_type = [u"6.8米", u"7.6米", u"9.6米", u"14.5米", u"17.5米"]
    url = "http://172.16.7.47:5001/v1/order_vehicles/dispatch/vehicle"
    re_data = {
        "order_number": str(order_number),
        "driver_name": u"小王",
        "driver_telephone": "13221124493",
        "antipate_arrive_time": str(datetime.now() + timedelta(hours=2))[:16],
        "vehicle_type": random.choice(plate_type)
    }
    truck_info = {
        "plate": u"沪C88888",
        "carriage_plate": u"",
        "carriage_length_type": "9.6",
        "carriage_type": u"高栏车",
        "send_vehicle_type": "1",
    }

    reqheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                  'Content-Type': 'application/json', 'token': "131ccd7e6e979858f77819c42a1e94d1", "shippersid": 203}

    re = request_sys(url, dict(re_data.items() + truck_info.items()), "POST", reqheaders)
    if not re or re['code'] != 1000:
        logger.info("result is {0}".format(re))

    truck_info = {
        "plate": u"陕Q12349",
        "carriage_plate": u"川HQ8092",
        "carriage_length_type": "9.6",
        "carriage_type": u"厢式车",
        "send_vehicle_type": "2",
    }
    re = request_sys(url, dict(re_data.items() + truck_info.items()), "POST", reqheaders)
    if not re or re['code'] != 1000:
        logger.info("result is {0}".format(re))


if __name__ == "__main__":
    # tasks = [gevent.spawn(inin_data) for i in range(2)]  # 启动协程
    # gevent.joinall(tasks)  # 停止协程
    # for i in xrange(1000):
    #     inin_data_order()
    origin_number = 2019042200002
    for i in range(1300):
        init_data_order_vehicles(origin_number + i)

