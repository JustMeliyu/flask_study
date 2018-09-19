# -*- coding:utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf8')
import traceback
import xlwt

from model.user import User
from model.driver import Driver
from model.line import Line
from model.truck import Truck
from model.rs_cq_trans import RS_CQ_Trans as rct
from model.transport_protocol import Transport_Protocol as tp
from model.transport_protocol_exception import Transport_Protocol_Exception as tpe
from model.qr_record import QR_Record as qr
from model.transport_protocol_relay import Transport_Protocol_Relay as tpr
from model.transport_protocol_flow import Transport_Protocol_Flow as tpf
from model.transport_protocol_cq import Transport_Protocol_Cq as tpc
from model.transport_protocol_note import Transport_Protocol_Note as tpn
from model.transport_departure_arrival_record import Transport_Departure_Arrival_Record as tdar
from model.jg_transport_departure_arrival_record import JG_Transport_Departure_Arrival_Record as jtdar
from instance.logger import logger

tp_status = {201: u'待签到', 300: u'待装车',
             500: u'运输中', 501: u'已完成', 301: u'已废止',
             503: u'异常确认', 502: u'人工完成', 302: u'无效运单',
             203: u'未绑定车头', 15: u'过时数据'}
run_mode = {0: u'单边车', 1: u'双边车'}
truck_type_dic = {0: u'高栏', 1: u'厢式'}
trucks_empty = {0: u'非空', 1: u'空车'}


def waybill_report(filename, addr, start_at, end_at, role_type, location_code):
    try:
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
        list_sheet1 = [u'序号', u'运单号', u'运单类型', u'司机姓名', u'手机号', u'司机姓名2', u'车牌号', u'车厢号牌',
                       u'线路', u'线路属性', u'车签(调度输入)', u'电子车签', u'单边车结算方式', u'结算车型',
                       u'装货签到日期', u'装货签到时间', u'预计发车日期', u'预计发车时间',
                       u'实际发车日期', u'实际发车时间', u'预计到达日期', u'预计到达时间', u'实际到车日期',
                       u'实际到车时间', u'车辆运行方式', u'运单创建日期',
                       u'运单创建时间', u'运单状态', u'备注', u'归属年份', u'承运商信息',
                       u'实际运行路线', u'应结算车型', u'是否放空返回',
                       u'是否一车往返', u'一车往返关联运单号', u'调度工号', u'调度姓名', u'车厢类型',
                       u'经停点1到车日期', u'经停点1到车时间', u'经停点1发车日期', u'经停点1发车时间',
                       u'经停点2到车日期', u'经停点2到车时间', u'经停点2发车日期', u'经停点2发车时间',
                       u'经停点3到车日期', u'经停点3到车时间', u'经停点3发车日期', u'经停点3发车时间',
                       u'经停点4到车日期', u'经停点4到车时间', u'经停点4发车日期', u'经停点4发车时间']

        list_sheet1 = [u'序号', u'运单号', u'运单类型', u'司机姓名', u'手机号', u'司机姓名2', u'车牌号', u'车厢号牌',
                       u'线路', u'线路属性', u'车签(调度输入)', u'电子车签', u'单边车结算方式', u'结算车型',
                       u'车辆运行方式', u'运单创建日期', u'运单创建时间', u'运单状态', u'铅封号', u'备注',
                       u'归属年份', u'承运商信息', u'实际运行路线', u'应结算车型', u'是否放空返回', u'是否一车往返',
                       u'一车往返关联运单号', u'调度工号', u'调度姓名', u'车厢类型',
                       u'装货签到日期', u'装货签到时间', u'预计发车日期', u'预计发车时间', u'实际发车日期', u'实际发车时间',
                       u'预计到达日期', u'预计到达时间', u'实际到车日期', u'实际到车时间', u'实际时效(新增)',
                       u'经停点1预计发车日期', u'经停点1预计发车时间', u'经停点1发车日期', u'经停点1发车时间',
                       u'经停点1预计到达日期', u'经停点1预计到达时间', u'经停点1到车日期', u'经停点1到车时间', u'经停点1实际时效',
                       u'经停点2预计发车日期', u'经停点2预计发车时间', u'经停点2发车日期', u'经停点2发车时间',
                       u'经停点2预计到达日期', u'经停点2预计到达时间', u'经停点2到车日期', u'经停点2到车时间', u'经停点2实际时效',
                       u'经停点3预计发车日期', u'经停点3预计发车时间', u'经停点3发车日期', u'经停点3发车时间',
                       u'经停点3预计到达日期', u'经停点3预计到达时间', u'经停点3到车日期', u'经停点3到车时间', u'经停点3实际时效',
                       u'经停点4预计发车日期', u'经停点4预计发车时间', u'经停点4发车日期', u'经停点4发车时间',
                       u'经停点4预计到达日期', u'经停点4预计到达时间', u'经停点4到车日期', u'经停点4到车时间', u'经停点4实际时效']
        for i in range(0, len(list_sheet1)):
            sheet1.write(0, i, list_sheet1[i])
        statement = "create_time >= '%s' and create_time < '%s'" % (start_at, end_at)
        trans = tp.query.filter(statement).all()
        i = 0
        for item in trans:
            i = i + 1
            try:
                list_trans = list()
                list_cq = list()
                list_note = list()
                location_list = list()
                trans_id = item.id
                trans_number = item.trans_number
                # tp_mode = ''
                line_name = ''
                relay_list = list()
                tp_mode = u'快递' if trans_number[0] == 'A' else u'快运'
                # if trans_number[0] == 'A':
                #     tp_mode = u'快递'
                # elif trans_number[0] == 'K':
                #     tp_mode = u'快运'
                # statement = " line_no = '%s' and line_status != 3 " % item.line_no
                line = item.line
                relayobjs = tpr.query.filter_by(trans_number=trans_number, location_code_type=2).all()
                if relayobjs:
                    for index in range(len(relayobjs)):
                        index += 1
                        relay = [relayobj for relayobj in relayobjs if getattr(relayobj, 'index') == index]
                        for obj in relay:
                            relay_list.append(obj.location_code)
                if role_type:
                    location_list.append(item.fk_at_location_code)
                    for index in range(len(relay_list)):
                        location_list.append(relay_list[index])
                    location_list.append(item.fk_to_location_code)
                if int(location_code) != 999999 and int(role_type) != 2:
                    if location_code not in location_list:
                        i = i - 1
                        continue
                # if int(location_code) == 999999 or int(role_type) == 2:
                #     pass
                # else:
                    # if location_code in location_list:
                    #     pass
                    # else:
                    #     i = i - 1
                    #     continue
                is_link = u'一车往返' if int(item.is_link) == 1 else ''
                # is_link = ''
                # if int(item.is_link) == 1:
                #     is_link = u'一车往返'
                link_tp = item.link
                plate = item.plate if item.plate else ''
                truck_licence = item.trailer_head if item.trailer_head else ''
                settlement_mode = item.settlement_mode
                start_date = str(item.start_time)[0:10]
                start_time = str(item.start_time)[10:30]
                end_date = str(item.end_time)[0:10]
                end_time = str(item.end_time)[10:30]
                depart_date = ''
                depart_time = ''
                reach_date = ''
                reach_time = ''
                driver_name = ''
                driver_tel = ''
                driver_name2 = ''
                cq_number_jg = ''
                truck_type = ''
                if item.run_mode == 0:
                    run_mode = u'单边车'
                elif item.run_mode == 1:
                    run_mode = u'双边车'
                else:
                    run_mode = ''
                belong_date = str(item.create_time)[0:7]
                create_date = str(item.create_time)[0:10]
                create_time = str(item.create_time)[10:30]
                carrier = u'%s' % str(item.carrier_name).strip() if item.carrier_name else ''
                true_line_name = ''
                true_settlement_mode = ''
                op_name = ''
                op_no = ''
                start_code = item.fk_at_location_code
                end_code = item.fk_to_location_code
                vehicle_type = str(item.vehicle_type).replace(u'米', '')
                truck_empty = ''
                check_date = ''
                check_time = ''
                line_pro = item.line_property
                if item.status == 200 and (item.fk_driver_id == '' or not item.fk_driver_id):
                    p_status = u'待接单'
                elif item.status == 200 and item.fk_driver_id:
                    p_status = u'始发未签到'
                else:
                    p_status = tp_status[item.status]
                if line:
                    line_name = line.line_name
                if not line_pro:
                    line_pro = line.line_property
                if relay_list and len(relay_list) > 0:
                    # if len(relay_list) > 0:
                    for index in range(len(relay_list)):
                        tdarobjs = tdar.query.filter_by(trans_number=trans_number,
                                                        fk_location_code=relay_list[index]).all()
                        if tdarobjs:
                            for tdarobj in tdarobjs:
                                if int(tdarobj.type) == 1:
                                    relay_arrival_date = str(tdarobj.status_time)[0:10]
                                    sheet1.write(i, 39 + index * 4, relay_arrival_date)
                                    relay_arrival_time = str(tdarobj.status_time)[10:30]
                                    sheet1.write(i, 40 + index * 4, relay_arrival_time)
                                elif int(tdarobj.type) == 2:
                                    relay_depart_date = str(tdarobj.status_time)[0:10]
                                    sheet1.write(i, 41 + index * 4, relay_depart_date)
                                    relay_depart_time = str(tdarobj.status_time)[10:30]
                                    sheet1.write(i, 42 + index * 4, relay_depart_time)
                if item.fk_driver_id and item.driver and item.driver.user:
                    driver_name = item.driver.user.fullname
                    driver_tel = item.driver.user.username
                # if item.fk_driver_id:
                #     if item.driver:
                #         if item.driver.user:
                #             driver_name = item.driver.user.fullname
                #             driver_tel = item.driver.user.username

                qr_obj2 = qr.query.filter_by(fk_trans_number=trans_number, operator_type=3).order_by(
                    qr.create_time.desc()).first()
                if qr_obj2:
                    user2 = Driver.query.filter_by(id=qr_obj2.fk_driver_id).first().user
                    if user2:
                        driver_name2 = user2.fullname

                tpcobj = tpc.query.filter_by(trans_number=trans_number).all()
                if tpcobj:
                    for cq in tpcobj:
                        if cq.cq_number:
                            list_cq.append(cq.cq_number)
                if item.rs_cq_trans:
                    cq_number_jg = item.rs_cq_trans.cq_number
                tdarobj = tdar.query.filter_by(trans_number=trans_number, fk_location_code=start_code, type=2).first()
                if int(item.status) == 502:
                    tpe_obj = tpe.query.filter_by(trans_number=trans_number, exception_status=2).first()
                    if tpe_obj:
                        logger.info("人工完成的数据")
                        depart_date = str(tpe_obj.depart_time)[0:10]
                        depart_time = str(tpe_obj.depart_time)[10:30]
                        reach_date = str(tpe_obj.arrive_time)[0:10]
                        reach_time = str(tpe_obj.arrive_time)[10:30]
                        logger.info(reach_date)
                        logger.info(reach_time)
                else:
                    if tdarobj:
                        depart_date = str(tdarobj.status_time)[0:10]
                        depart_time = str(tdarobj.status_time)[10:30]
                    tdarobj = tdar.query.filter_by(trans_number=trans_number, fk_location_code=end_code, type=1).first()
                    if tdarobj:
                        reach_date = str(tdarobj.status_time)[0:10]
                        reach_time = str(tdarobj.status_time)[10:30]
                tpf_200 = tpf.query.filter_by(fk_trans_number=trans_number, status=200).first()
                if tpf_200:
                    if tpf_200.operator:
                        op_no = tpf_200.operator.user_no
                        op_name = tpf_200.operator.fullname
                if item.plate:
                    statement = "plate='%s' and if_valid = 1" % item.plate
                    truck_Valid = Truck.query.filter(statement).first()
                    if truck_Valid:
                        truck_type = truck_type_dic.get(truck_Valid.type, '')
                        # try:
                        #     truck_type = truck_type_dic[truck_Valid.type]
                        # except KeyError:
                        #     truck_type = ''
                        if not carrier:
                            carrier = truck_Valid.carrier_name
                        if not run_mode:
                            if truck_Valid.run_mode == 0:
                                run_mode = u'单边车'
                            elif truck_Valid.run_mode == 1:
                                run_mode = u'双边车'
                        if not vehicle_type and truck_Valid.vehicle_type[-1] != u'米':
                            vehicle_type = truck_Valid.vehicle_type + u'米'
                        elif not vehicle_type:
                            vehicle_type = truck_Valid.vehicle_type
                transport_protocol_notes = tpn.query.filter_by(fk_trans_number=trans_number).all()
                if transport_protocol_notes:
                    for transport_protocol_note in transport_protocol_notes:
                        if transport_protocol_note.note_type == 2:  # 备注
                            list_note.append('  ' + transport_protocol_note.note)
                        if not truck_licence and transport_protocol_note.note_type == 3:
                            truck_licence = transport_protocol_note.note
                            list_note.append('  ' + transport_protocol_note.note)
                        if transport_protocol_note.note_type == 4:
                            true_settlement_mode = str(transport_protocol_note.note).replace(u'米', '')
                            list_note.append('  ' + transport_protocol_note.note)
                        if transport_protocol_note.note_type == 5:  # 实际运行线路
                            true_line_name = transport_protocol_note.note
                            list_note.append('  ' + transport_protocol_note.note)
                        if transport_protocol_note.note_type == 6:
                            truck_empty = trucks_empty[int(transport_protocol_note.note)]
                            list_note.append('  ' + truck_empty)
                        if not transport_protocol_note.note_type:
                            list_note.append('  ' + transport_protocol_note.note)
                tpf_check = tpf.query.filter_by(fk_trans_number=trans_number, status=300).first()
                if tpf_check:
                    check_date = str(tpf_check.status_time)[0:10]
                    check_time = str(tpf_check.status_time)[10:30]
                list_trans.append(trans_id)
                list_trans.append(trans_number)
                list_trans.append(tp_mode)
                list_trans.append(driver_name)
                list_trans.append(driver_tel)
                list_trans.append(driver_name2)
                list_trans.append(plate)
                list_trans.append(truck_licence)
                list_trans.append(line_name)
                list_trans.append(line_pro)
                list_trans.append(list_cq)
                list_trans.append(cq_number_jg)
                list_trans.append(settlement_mode)
                list_trans.append(vehicle_type)
                # 以上未顺序未变
                list_trans.append(check_date)
                list_trans.append(check_time)
                list_trans.append(start_date)
                list_trans.append(start_time)
                list_trans.append(depart_date)
                list_trans.append(depart_time)
                list_trans.append(end_date)
                list_trans.append(end_time)
                list_trans.append(reach_date)
                list_trans.append(reach_time)
                list_trans.append(run_mode)
                list_trans.append(create_date)
                list_trans.append(create_time)
                list_trans.append(p_status)
                list_trans.append(list_note)
                list_trans.append(belong_date)
                list_trans.append(carrier)
                list_trans.append(true_line_name)
                list_trans.append(true_settlement_mode)
                list_trans.append(truck_empty)
                list_trans.append(is_link)
                list_trans.append(link_tp)
                list_trans.append(op_no)
                list_trans.append(op_name)
                list_trans.append(truck_type)
                for j in xrange(len(list_trans)):
                    sheet1.write(i, j, list_trans[j])
            except:
                logger.error('the error trans_number is %s' % trans_number)
                logger.error('report catch exception %s' % traceback.format_exc())
                sheet1.write(i, 0, trans_id)
                sheet1.write(i, 1, trans_number)
                sheet1.write(i, 2, u'数据异常')
        workbook.save(addr + filename)
        return 1000
    except:
        logger.error('report catch exception %s' % traceback.format_exc())
        return 1001
