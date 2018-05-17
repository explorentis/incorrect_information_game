# -*- coding: utf-8 -*-
# Copyright © 2018 Sergei Kuznetsov. All rights reserved.
import commands


def run_game(world):
    new_turn = True
    while not world.quit:
        for c in world.companies:
            if (((not new_turn) and (not c.turn_finished)) or new_turn):
                c.get_command()
                a = c.director.last_command.split(' ')
                cmd = a[0]
                if len(a) == 2:
                    value = a[1]
                else:
                    value = 1
                if cmd in commands.commands_list.keys():
                    commands.commands_list[cmd](world, c, int(value))
                else:
                    strings.send_text(strigs.COMMAND_IS_NOT_EXIST % c.name)
                if not c.turn_finished:
                    new_turn = False
        new_turn = True
        for c in world.companies:
            if not c.turn_finished:
                new_turn = False
        if new_turn:
            world.ontime()
            for c in world.companies:
                c.turn_finished = False
