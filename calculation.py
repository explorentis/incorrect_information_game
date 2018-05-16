# -*- coding: utf-8 -*-
# Copyright © 2018 Sergei Kuznetsov. All rights reserved.
# Модуль рассчета оптимальных параметров в заданном алгоритме
import commands

from company import Company

from director import Director

from world import World


def recur_calc(parameters_list,
               pos,
               parameters,
               current_val,
               nrun,
               logfile,
               player):
    for i in range(parameters[parameters_list[pos]][0],
                   parameters[parameters_list[pos]][1]):
        current_val[parameters_list[pos]] = i
        if len(parameters_list) - 1 != pos:
            recur_calc(parameters_list,
                       pos + 1,
                       parameters,
                       current_val,
                       nrun,
                       logfile,
                       player)
        else:
            n = nrun
            wins = 0
            loses = 0
            while n != 0:
                world = World([
                    Company(Director(player, current_val))
                ], hideoutput=True)

                new_turn = True
                while not world.quit:
                    for c in world.companies:
                        if (((not new_turn) and (not c.turn_finished))
                                or new_turn):

                            c.get_command()
                            a = c.director.last_command.split(' ')
                            cmd = a[0]
                            if len(a) == 2:
                                value = a[1]
                            else:
                                value = 1
                            if cmd in commands.commands_list.keys():
                                commands.commands_list[cmd](world,
                                                            c,
                                                            int(value))
                            else:
                                print('%s: нет такой команды' % c.name)
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
                if world.winner_is_here:
                    wins += 1
                else:
                    loses += 1
                n -= 1
            print('Побед: %d из %d с заданными параметрами %s'
                  % (wins, nrun, str(current_val)))
            logfile.write('Побед: %d из %d с заданными параметрами %s'
                          % (wins, nrun, str(current_val)))


# players - указатель на функцию игрока
# nruns - количество миров для каждой комбинации параметров
# parameters - словарь переменных, используемых в данной функции. Представляет
# из себя:
# {obj.var1: (minval, maxval), obj.var2: (minval, maxval)}
def calc(player, nruns, parameters):
    logfile = open('lastresults.log', 'w')
    keys = []
    current_val = {}
    for key in parameters.keys():
        keys.append(key)
    recur_calc(keys, 0, parameters, current_val, nruns, logfile, player)
    logfile.close()
