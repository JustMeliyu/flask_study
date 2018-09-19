# -*- coding:utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf8')
import traceback
import xlwt
from datetime import datetime
from sqlalchemy import text
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
# run_mode = {0: u'单边车', 1: u'双边车'}
truck_type_dic = {0: u'高栏', 1: u'厢式'}
trucks_empty = {0: u'非空', 1: u'空车'}


def waybill_report(filename, addr, start_at, end_at, role_type, location_code):
    try:
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
        list_sheet1 = [u'序号', u'运单号', u'运单类型', u'司机姓名', u'手机号', u'司机姓名2', u'车牌号', u'车厢号牌',
                       u'线路', u'线路属性', u'车签(调度输入)', u'电子车签', u'单边车结算方式', u'结算车型',
                       u'车辆运行方式', u'运单创建日期', u'运单创建时间', u'运单状态', u'铅封号', u'备注',
                       u'归属年份', u'承运商信息', u'实际运行路线', u'应结算车型', u'是否放空返回', u'是否一车往返',
                       u'一车往返关联运单号', u'调度工号', u'调度姓名', u'车厢类型',
                       u'装货签到日期', u'装货签到时间', u'预计发车日期', u'预计发车时间', u'实际发车日期', u'实际发车时间',
                       u'预计到达日期', u'预计到达时间', u'实际到车日期', u'实际到车时间', u'实际时效',
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
        trans = tp.query.filter(text(statement)).all()
        i = 0
        for item in trans:
            i = i + 1
            trans_id = item.id
            try:
                list_trans = list()
                # 第一组
                trans_number = item.trans_number
                tp_mode = u'快递' if trans_number[0] == 'A' else u'快运'
                driver_name = ''
                driver_tel = ''
                driver_name2 = ''
                if item.fk_driver_id and item.driver and item.driver.user:
                    driver_name = item.driver.user.fullname
                    driver_tel = item.driver.user.username
                qr_obj2 = qr.query.filter_by(fk_trans_number=trans_number, operator_type=3).order_by(
                    qr.create_time.desc()).first()
                if qr_obj2:
                    user2 = Driver.query.filter_by(id=qr_obj2.fk_driver_id).first().user
                    if user2:
                        driver_name2 = user2.fullname
                plate = item.plate if item.plate else ''
                truck_licence = item.trailer_head if item.trailer_head else ''

                # 第二组
                line = item.line
                line_name = line.line_name if line else ''
                line_pro = item.line_property if item.line_property else line.line_property
                list_cq = list()
                tpcobj = tpc.query.filter_by(trans_number=trans_number).all()
                if tpcobj:
                    for cq in tpcobj:
                        if cq.cq_number:
                            list_cq.append(cq.cq_number)
                cq_number_jg = item.rs_cq_trans.cq_number if item.rs_cq_trans else ''
                settlement_mode = item.settlement_mode
                vehicle_type = str(item.vehicle_type).replace(u'米', '')
                carrier = u'%s' % str(item.carrier_name).strip() if item.carrier_name else ''
                if item.run_mode == 0:
                    run_mode = u'单边车'
                elif item.run_mode == 1:
                    run_mode = u'双边车'
                else:
                    run_mode = ''
                truck_type = ''
                if item.plate:
                    statement = "plate='%s' and if_valid = 1" % item.plate
                    truck_Valid = Truck.query.filter(text(statement)).first()
                    if truck_Valid:
                        truck_type = truck_type_dic.get(truck_Valid.type, '')
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

                # 第三组
                # run_mode
                create_date = str(item.create_time)[0:10]
                create_time = str(item.create_time)[10:30]
                if item.status == 200 and (item.fk_driver_id == '' or not item.fk_driver_id):
                    p_status = u'待接单'
                elif item.status == 200 and item.fk_driver_id:
                    p_status = u'始发未签到'
                else:
                    p_status = tp_status[item.status]
                # 铅封号
                seal_no = ''
                list_note = ''
                seal_nos = tpn.query.filter_by(fk_trans_number=trans_number).all()
                if seal_nos:
                    for sn in seal_nos:
                        if sn.note_type == 8:           # 铅封号
                            seal_no += (sn.note + ',')
                        elif sn.note_type == 2:         # 备注
                            list_note += (sn.note + ';')
                seal_no = seal_no[:-1]
                list_note = list_note[:-1] if len(list_note) <= 120 else list_note[:120]
                belong_date = str(item.create_time)[0:7]
                # carrier
                true_line_name = ''
                true_settlement_mode = ''
                truck_empty = ''
                is_link = u'一车往返' if int(item.is_link) == 1 else ''
                link_tp = item.link
                op_name = ''
                op_no = ''
                tpf_200 = tpf.query.filter_by(fk_trans_number=trans_number, status=200).first()
                if tpf_200 and tpf_200.operator:
                    op_no = tpf_200.operator.user_no
                    op_name = tpf_200.operator.fullname
                # truck_type

                # 第四组
                tpf_check = tpf.query.filter_by(fk_trans_number=trans_number, status=300).first()
                check_date = str(tpf_check.status_time)[0:10] if tpf_check else ''
                check_time = str(tpf_check.status_time)[10:30] if tpf_check else ''
                start_date = str(item.start_time)[0:10]
                start_time = str(item.start_time)[10:30]
                start_code = item.fk_at_location_code
                end_code = item.fk_to_location_code
                depart_date = ''
                depart_time = ''
                reach_date = ''
                reach_time = ''
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
                end_full_time = ''
                if depart_time and depart_date:
                    depart_full_time = datetime.strptime(depart_date + '' + depart_time, "%Y-%m-%d %H:%M:%S")
                    end_t = datetime.strptime(item.end_time, "%Y-%m-%d %H:%M")
                    start_t = datetime.strptime(item.start_time, "%Y-%m-%d %H:%M")
                    end_full_time = depart_full_time + (end_t - start_t)
                end_date = str(end_full_time)[0:10] if end_full_time else ''
                end_time = str(end_full_time)[10:30] if end_full_time else ''
                # 实际时效
                actual_prescription = ''
                if end_full_time and reach_date and reach_time:
                    reach_full_time = datetime.strptime(reach_date + '' + reach_time, "%Y-%m-%d %H:%M:%S")
                    actual_prescription = format((end_full_time - reach_full_time).seconds / 60, '.2f')

                # 第五组
                location_list = list()
                relay_list = list()
                # 经停点信息
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
                if location_list and len(location_list) > 0:
                    for index in range(len(location_list)):
                        if index != 0:
                            point_end_t = ''
                            pro_tdarobj = tdar.query.filter_by(trans_number=trans_number, type=2,
                                                               fk_location_code=location_list[index - 1]).first()
                            pro_arrival_t = pro_tdarobj.status_time if pro_tdarobj else ''

                            pro_tpr = tpr.query.filter_by(trans_number=trans_number,
                                                          location_code=location_list[index - 1]).first()
                            cur_tpr = tpr.query.filter_by(trans_number=trans_number,
                                                          location_code=location_list[index]).first()
                            # 预计到达和预计发车时间
                            if cur_tpr and cur_tpr.start_time:
                                point_start_date = str(cur_tpr.start_time)[0:10]
                                point_start_time = str(cur_tpr.start_time)[10:30]
                                sheet1.write(i, 41 + (index - 1) * 9, point_start_date)
                                sheet1.write(i, 42 + (index - 1) * 9, point_start_time)
                            if pro_arrival_t and pro_tpr and cur_tpr and pro_tpr.start_time and cur_tpr.end_time:
                                cur_end_t = datetime.strptime(cur_tpr.end_time, "%Y-%m-%d %H:%M")
                                pro_end_t = datetime.strptime(pro_tpr.start_time, "%Y-%m-%d %H:%M")
                                point_end_t = pro_arrival_t + (cur_end_t - pro_end_t)
                                point_end_date = str(point_end_t)[0:10]
                                point_end_time = str(point_end_t)[10:30]
                                sheet1.write(i, 45 + (index - 1) * 9, point_end_date)
                                sheet1.write(i, 46 + (index - 1) * 9, point_end_time)
                            # 实际到达与实际发车时间
                            tdarobjs = tdar.query.filter_by(trans_number=trans_number,
                                                            fk_location_code=location_list[index]).all()
                            if tdarobjs:
                                for tdarobj in tdarobjs:
                                    if int(tdarobj.type) == 1:
                                        relay_arrival_date = str(tdarobj.status_time)[0:10]
                                        relay_arrival_time = str(tdarobj.status_time)[10:30]
                                        sheet1.write(i, 47 + (index - 1) * 9, relay_arrival_date)
                                        sheet1.write(i, 48 + (index - 1) * 9, relay_arrival_time)
                                        if point_end_t:
                                            point_prescription = format((point_end_t - tdarobj.status_time).seconds / 60
                                                                        , ".2f")
                                            sheet1.write(i, 49 + (index - 1) * 9, point_prescription)
                                    elif int(tdarobj.type) == 2:
                                        relay_depart_date = str(tdarobj.status_time)[0:10]
                                        sheet1.write(i, 43 + (index - 1) * 9, relay_depart_date)
                                        relay_depart_time = str(tdarobj.status_time)[10:30]
                                        sheet1.write(i, 44 + (index - 1) * 9, relay_depart_time)

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
                list_trans.append(run_mode)
                list_trans.append(create_date)
                list_trans.append(create_time)
                list_trans.append(p_status)
                list_trans.append(seal_no)
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
                list_trans.append(actual_prescription)
                for j in xrange(len(list_trans)):
                    sheet1.write(i, j, list_trans[j])
            except:
                logger.error('the error trans_number is %s' % trans_number)
                logger.error('report catch exception %s' % traceback.format_exc())
                sheet1.write(i, 0, trans_id)
                sheet1.write(i, 1, trans_number)
                sheet1.write(i, 2, u'数据异常')
        print addr + filename
        workbook.save(addr + filename)
        return 1000
    except:
        logger.error('report catch exception %s' % traceback.format_exc())
        return 1001
