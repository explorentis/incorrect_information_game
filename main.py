# -*- coding: utf-8 -*-
from random import choice
from world import World
from company import Company

def quit_game(world, company):
    world.quit = True

def help(world, company):
    print('''Список комманд:
    q - выход,
    h - эта помощь,
    s - информация о Вашем бизнесе,
    w - ждать следующей даты,
    gw - взять деньги в долг, требуется 1 ход,
    rw - вернуть деньги, требуется 1 ход,
    b - купить товар,
    d - продать товар,
    sf - вывести инфо обо всех организациях''')

def get_money(world, company):
    company.money += 1
    company.credit += 1
    company.turn_finished = True

def return_money(world, company):
    if company.money < 1:
        if  company.show_messages:
            print('%s: Недостаточно денег!' % company.name)
        return
    company.money -= 1
    company.credit -= 1
    company.turn_finished = True

def buy(world, company):
    if company.money < world.price:
        if  company.show_messages:
            print('%s: Недостаточно денег!' % company.name)
        return
    company.money -= world.price
    company.goody += 1
    company.turn_finished = True
    
def sell(world, company):
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

def world_info(world, company):
    world.info()

def world_info_forced(world, company):
    world.info(True)

    
def world_ontime(world, company):
    company.turn_finished = True
    
def player_command():
    return input('you@yourbussiness> ')

aicmd = ['w', 'gw', 'rw', 'b', 'd']

def random_command():
    return choice(['w', 'gw', 'rw', 'b', 'd'])

world = World([
    Company(player_command, True),
    Company(random_command),
    Company(random_command),
    Company(random_command)
])


commands = {
    'q': quit_game,
    'h': help,
    's': world_info,
    'w': world_ontime,
    'gw': get_money,
    'rw': return_money,
    'b': buy,
    'd': sell,
    'sf': world_info_forced
}


new_turn = True
while not world.quit:
    for c in world.companies:
        if (((new_turn == False) and (c.turn_finished == False)) or new_turn == True):
            c.get_command()
            if c.last_command in commands.keys():
                commands[c.last_command](world, c)
            else:
                print("%s: нет такой команды" % c.name)
            if c.turn_finished == False:
                new_turn = False
    new_turn = True
    for c in world.companies:
        if c.turn_finished == False:
            new_turn = False
    if new_turn == True:
        world.ontime()
        for c in world.companies:
            c.turn_finished = False
