# encoding:utf-8
import xlrd
import sys
import numpy
reload(sys)
sys.setdefaultencoding('utf-8')
formula = {
    u"浙江": {
        0: lambda x, t: 0.09 * x * t,
        15: lambda x, t: (0.12 - 0.002 * t) * x * t,
        30: lambda x, t: 0.06 * x * t,
    },
    u"上海": {
      0: lambda x, t: 0.6 * x,
      2: lambda x, t: 0.9 * x,
      5: lambda x, t: 1.02 * x,
      10: lambda x, t: 1.315 * x,
      15: lambda x, t: 1.428 * x,
    },
    u"江苏": {
        0: lambda x, t: 0.09 * x * t,
        10: lambda x, t: (8 / 75 - t / 600) * x * t,
        40: lambda x, t: 0.04 * x * t,
    },
    u"安徽": {
        0: lambda x, t: 0.09 * x * t,
        10: lambda x, t: (31 / 300 - t / 750) * x * t,
        40: lambda x, t: 0.05 * x * t,
    },
    u"江西": {
        0: lambda x, t: 0.09 * x * t,
        10: lambda x, t: (0.105 - 0.0015 * t) * x * t,
        40: lambda x, t: 0.045 * x * t,
    },
}
START_ROW = 2           # 起始行
ACTUAL_PRICE_COL = 2    # 实际价格所在列
DISTINCE_COL = 3        # 距离所在列
WEIGHT_COL = 4          # 重量所在列
MIN_DEVIATION = -0.1    # 最小偏移比例
MAX_DEVIATION = 0.1     # 最大偏移比例
PRE_DEVIATION = 0.01    # 单次偏移比例


def calculation(file_addr, province, sheet_name):
    pro_data = formula.get(province)
    if pro_data is None:
        print(u"省份不存在, 当前省份为 is {0} !!!".format(province))
        return None, None
    try:
        workbook = xlrd.open_workbook(file_addr)
        print(u"当前处理工作簿地址为: {0}".format(file_addr))
    except IOError:
        print u"当前处理工作簿不存在, 地址为: {0}".format(file_addr)
        return None, None
    try:
        ws = workbook.sheet_by_name(sheet_name)
        print(u"当前处理工作表名称为: {0}".format(sheet_name))
    except:
        print(u"当前处理工作表不存在, 名称为: {0}".format(sheet_name))
        return None, None

    actual_prices = ws.col_values(ACTUAL_PRICE_COL - 1, START_ROW - 1)
    distinces = ws.col_values(DISTINCE_COL - 1, START_ROW - 1)
    weights = ws.col_values(WEIGHT_COL - 1, START_ROW - 1)
    all_data = list()

    for i in range(len(actual_prices)):
        try:
            all_data.append([float(actual_prices[i]), float(distinces[i]) / 1000, float(weights[i]) / 1000])
        except:
            print(u"第 {0} 行数据格式错误, 跳过该值!".format(START_ROW + i))
    weight_range = sorted(pro_data.keys())
    all_squre = list()
    min_squre = 100000000000000000
    min_weight_deviation = min_distince_deviation = 0
    for distince_deviation in numpy.arange(MIN_DEVIATION, MAX_DEVIATION, PRE_DEVIATION):
        distince_deviation = round(distince_deviation, 2)
        for weight_deviation in numpy.arange(MIN_DEVIATION, MAX_DEVIATION, PRE_DEVIATION):
            weight_deviation = round(weight_deviation, 2)
            current_square = 0
            for data in all_data:
                pre_range = 0
                # 获取重量范围及计算公式
                for i in weight_range:
                    if i > data[2]:
                        break
                    pre_range = i
                pre_formula = pro_data.get(pre_range)
                # 计算平方差
                require_price = pre_formula(data[1] * (1 + distince_deviation), data[2] * (1 + weight_deviation))
                current_square += abs(data[0] * data[0] - require_price * require_price)
            all_squre.append([current_square, distince_deviation, weight_deviation])
            if current_square < min_squre:
                min_distince_deviation = distince_deviation
                min_weight_deviation = weight_deviation
                min_squre = current_square
    print(u"最小距离便移比例为 {0}, 最小重量便移比例为 {1}, 便移平方差为 {2}".
          format(min_distince_deviation, min_weight_deviation, min_squre))
    return min_distince_deviation, min_weight_deviation


if __name__ == "__main__":
    dis_deviation, wei_deviation = calculation(u"./五省数据.xlsx", u"上海", u"上海")
