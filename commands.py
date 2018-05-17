# -*- coding: utf-8 -*-
# Copyright © 2018 Sergei Kuznetsov. All rights reserved.

# Список команд управления
from random import randint

import strings
# Не забывать про словарь commands в конце этого файла!!!


def quit_game(world, company, value=None):
    world.quit = True


def help_game(world, company, value=None):
    strings.send_text(strings.HELP_TEXT)


def get_money(world, company, value=1):
    company.money += value
    company.credit += value
    company.turn_finished = True


def return_money(world, company, value=1):
    if company.money < value:
        if company.show_messages:
            strings.send_text(strings.INSUFFICIENT_MONEY % company.name)
        return
    if company.credit < value:
        value = company.credit
    company.money -= value
    company.credit -= value
    company.turn_finished = True


def buy(world, company, value=1):
    if company.money < (value * world.price):
        if company.show_messages:
            strings.send_text(strings.INSUFFICIENT_MONEY % company.name)
        return
    company.money -= (value * world.price)
    company.goody += value
    company.turn_finished = True


def sell(world, company, value=None):
    count = 0
    sell_price = 0
    while (randint(0, 3) != 0) and (company.goody > 0):
        company.goody -= 1
        sell_price = int(world.price * 1.2) + 1
        company.money += sell_price
        count += 1
    if company.show_messages:
        strings.send_text(strings.SUCCESS_TRADE % (company.name,
                                                   count,
                                                   sell_price,
                                                   count * sell_price))
    company.turn_finished = True


def world_info(world, company, value=None):
    world.info()


def world_info_forced(world, company, value=None):
    world.info(True)


def world_ontime(world, company, value=None):
    company.turn_finished = True


commands_list = {
    'q': quit_game,
    'h': help_game,
    's': world_info,
    'w': world_ontime,
    'gw': get_money,
    'rw': return_money,
    'b': buy,
    'd': sell,
    'sf': world_info_forced
}
