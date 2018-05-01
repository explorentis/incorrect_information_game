# -*- coding: utf-8 -*-
from random import choice
from world import World
from company import Company
from commands import *
    
def player_command():
    return input('you@yourbussiness> ')

aicmd = ['w', 'gw', 'rw', 'b', 'd']

def random_command():
    return choice(aicmd)

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
