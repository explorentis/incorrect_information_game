# -*- coding: utf-8 -*-
from random import choice
from world import World
from company import Company
from commands import *
    
def semiai_command(company):
    if (company.money < company.world.price) and (company.goody == 0):
        return 'gw 70'
    elif (company.credit + (company.world.price * 5) < company.money) and (company.credit > 0):
        return 'rw ' + str(company.credit)
    elif (company.credit > 70) and (company.goody > 5):
        return 'rw ' + str(company.money)
    elif (company.money != 0) and (company.goody == 0):
        return 'b ' + str(int(company.money /(2 * company.world.price)))
    elif company.goody != 0:
        return 'd'
    else:
        return 'w'
    
def player_command(company):
    return input('you@yourbussiness> ')

aicmd = ['w', 'gw', 'rw', 'b', 'd']

def random_command(company):
    return choice(aicmd)

world = World([
    Company(semiai_command),
    Company(semiai_command, True),
    Company(player_command, True),
    Company(random_command, True),
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
    #input('waiting...>')
    for c in world.companies:
        if (((new_turn == False) and (c.turn_finished == False)) or new_turn == True):
            c.get_command()
            a = c.last_command.split(' ')
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
