# -*- coding: utf-8 -*-
from random import choice
from world import World
from company import Company
from commands import *


class Director:
    def __init__(self, command_function):
        self.command = command_function
        self.company = None
        self.last_command = None
    
    def get_command(self):
        self.last_command = self.command(self)

    
def semiai_command(director):
    money = director.company.money
    price = director.company.world.price
    product_amount = director.company.goody
    credit = director.company.credit
    if (money < price) and (product_amount == 0):
        return 'gw 70'
    elif (credit + (price * 5) < money) and (credit > 0):
        return 'rw ' + str(credit)
    elif (credit > 70) and (product_amount > 5):
        return 'rw ' + str(money)
    elif (money != 0) and (product_amount == 0):
        return 'b ' + str(int(money /(2 * price)))
    elif product_amount != 0:
        return 'd'
    else:
        return 'w'
    
def player_command(director):
    return input('you@yourbussiness> ')

world = World([
    # Company(semiai_command),
    Company(Director(semiai_command), True),
    # Company(Director(player_command), True)
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
            a = c.director.last_command.split(' ')
            cmd = a[0]
            if len(a) == 2:
                value = a[1]
            else:
                value = 1
            if cmd in commands.keys():
                commands[cmd](world, c, int(value))
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
