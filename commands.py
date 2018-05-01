# -*- coding: utf-8 -*-
# Список команд управления
from random import choice

def quit_game(world, company, value=None):
    world.quit = True

def help(world, company, value=None):
    print('''Список комманд:
    q - выход,
    h - эта помощь,
    s - информация о Вашем бизнесе,
    w - ждать следующей даты,
    gw [сумма] - взять деньги в долг, требуется 1 ход,
    rw [сумма] - вернуть деньги, требуется 1 ход,
    b [количество товара] - купить товар, 1 ход,
    d - продать товар, 1 ход, продать пытаются всегда максимально возможное количество
    sf - вывести инфо обо всех организациях''')

def get_money(world, company, value=1):
    company.money += value
    company.credit += value
    company.turn_finished = True

def return_money(world, company, value=1):
    if company.money < value:
        if  company.show_messages:
            print('%s: Недостаточно денег!' % company.name)
        return
    company.money -= value
    company.credit -= value
    company.turn_finished = True

def buy(world, company, value=1):
    if company.money < (value * world.price):
        if  company.show_messages:
            print('%s: Недостаточно денег!' % company.name)
        return
    company.money -= (value * world.price)
    company.goody += value
    company.turn_finished = True
    
def sell(world, company, value=None):
    count = 0
    sell_price = 0
    while (choice('yn') == 'y') and (company.goody > 0):
        company.goody -= 1
        sell_price = int(world.price * 1.2) + 1
        company.money += sell_price
        count += 1
    if  company.show_messages:
        print("%s: Вы продали %d товаров по цене %d на сумму %d" 
              % (company.name, count, sell_price, count * sell_price))
    company.turn_finished = True

def world_info(world, company, value=None):
    world.info()

def world_info_forced(world, company, value=None):
    world.info(True)

    
def world_ontime(world, company, value=None):
    company.turn_finished = True
