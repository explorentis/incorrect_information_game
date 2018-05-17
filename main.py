# -*- coding: utf-8 -*-
# Copyright © 2018 Sergei Kuznetsov. All rights reserved.
from company import Company

from director import Director

from game import run_game

import players

import strings

from world import World

answer = input(strings.MAINMENU_TEXT)

if answer == '1':
    player_count = input(strings.PLAYER_COUNT)
    company_list = []
    for i in range(0, int(player_count)):
        strings.send_text(strings.PLAYER_SELECT % (i + 1))
        for j in range(0, len(players.players_list)):
            strings.send_text('%d) %s' % (j + 1, players.players_list[j]))
        selected_player = int(input(strings.INPUT_NUMBER)) - 1
        visible_info = input(strings.SHOW_HIS_TURNS)
        if visible_info == '1':
            visible_info = True
        else:
            visible_info = False
        company_list.append(
            Company(Director(players.func_list[selected_player]),
                    visible_info))

    world = World(company_list)
    run_game(world)
elif answer == '2':
    from calculation import calc
    from players.semiai import semiai_command
    calc(semiai_command, 100, {'credit_sum': (70, 90),
                               'money_for_product_reserve': (0, 10)})
else:
    strings.send_text(strings.BYE)
    try:
        exit(0)
    except SystemExit:
        strings.send_text(strings.SYSTEMEXIT_EXCEPTION)
