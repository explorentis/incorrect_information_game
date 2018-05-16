# -*- coding: utf-8 -*-
# Copyright © 2018 Sergei Kuznetsov. All rights reserved.
from company import Company

from director import Director

from game import run_game

import players

from world import World

answer = input('Это экономическая игра, в которой вы управляете предприятием\n\
Для того, чтобы получить больше информации (в том числе и о правилах игры)\
загляните в файл README.txt\n\
Укажите, что хотите:\n\
                1) Запустить игру\n\
                2) Расчитать параметры для AI, написанного Вами(см.howtodev)\n\
любой другой ввод) Выход\n\
Ваш выбор> ')

if answer == '1':
    player_count = input('Введите количество игроков> ')
    company_list = []
    for i in range(0, int(player_count)):
        print('Игрок %d. Выберите, кто будет им управлять:' % (i + 1))
        for j in range(0, len(players.players_list)):
            print('%d) %s' % (j + 1, players.players_list[j]))
        selected_player = int(input('Введите номер> ')) - 1
        print(selected_player)
        visible_info = input('Вы хотите видить его ходы? (1 - да) > ')
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
    print('Пока!')
    try:
        exit(0)
    except SystemExit:
        print('Вы поймали SystemExit, вероятно Вы запустили это приложение\
через IDLE или Wing')
