# -*- coding: utf-8 -*-
# Copyright © 2018 Sergei Kuznetsov. All rights reserved.


def semiai_command(director):
    money = director.company.money
    price = director.company.world.price
    product_amount = director.company.goody
    credit = director.company.credit

    credit_sum = director.parameters['credit_sum']
    money_for_prod_reserve = director.parameters['money_for_product_reserve']

    # Если денег нет и товара нет - берем в долг фиксированную сумму
    if (money < price) and (product_amount == 0):
        return 'gw ' + str(credit_sum)
    # если денег больше, чем долг + запас
    elif (credit + (price * money_for_prod_reserve) < money) and (credit > 0):
        return 'rw ' + str(credit)
    elif (credit > credit_sum) and (product_amount > money_for_prod_reserve):
        return 'rw ' + str(money)
    elif (money != 0) and (product_amount == 0):
        return 'b ' + str(int(money / (2 * price)))
    elif product_amount != 0:
        return 'd'
    else:
        return 'w'
