# encoding: utf-8
"""一瓶汽水1元，两个瓶子可换一瓶汽水，20元最多喝多少汽水"""

coke_price = 1
totle_money = 20


def get_coke(money):
    totle_bottle = 0
    current_bottle = 0
    while money != 0:
        money -= 1
        totle_bottle += 1
        current_bottle += 1
        if current_bottle == 2:
            totle_bottle += 1
            current_bottle = 1
    return totle_bottle


print get_coke(20)


def get_coke2(bottle):

    if bottle == 1:
        return 0
    return bottle // 2 + get_coke2(bottle // 2 + bottle % 2)


print 20 + get_coke2(20)
