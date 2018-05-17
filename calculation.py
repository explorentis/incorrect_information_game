# -*- coding: utf-8 -*-
# Copyright © 2018 Sergei Kuznetsov. All rights reserved.
# Модуль рассчета оптимальных параметров в заданном алгоритме
from company import Company

from director import Director

from game import run_game

import strings

from world import World


def recur_calc(parameters_list,
               pos,
               parameters,
               current_val,
               nrun,
               logfile,
               player,
               top_score=[]):
    top_plays = top_score
    min_value = parameters[parameters_list[pos]][0]
    max_value = parameters[parameters_list[pos]][1]
    for i in range(min_value, max_value):
        current_val[parameters_list[pos]] = i
        if len(parameters_list) - 1 != pos:
            top_plays = recur_calc(parameters_list,
                                   pos + 1,
                                   parameters,
                                   current_val,
                                   nrun,
                                   logfile,
                                   player,
                                   top_plays)
        else:
            n = nrun
            wins = 0
            loses = 0
            while n != 0:
                world = World([
                    Company(Director(player, current_val))
                ], hideoutput=True)

                run_game(world)

                if world.winner_is_here:
                    wins += 1
                else:
                    loses += 1
                n -= 1
            strings.send_text(strings.AI_WIN_RESULT % (wins,
                                                       nrun,
                                                       str(current_val),
                                                       ''))
            logfile.write(strings.AI_WIN_RESULT
                          % (wins, nrun, str(current_val), '\n'))
            if top_plays:
                if wins < top_plays[0]:
                    pass
                else:
                    if len(top_plays) < 10:
                        top_plays.append(wins)
                    else:
                        top_plays[0] = wins
            else:
                top_plays.append(wins)
            top_plays.sort()
    return top_plays


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
    top_plays = recur_calc(keys,
                           0,
                           parameters,
                           current_val,
                           nruns,
                           logfile,
                           player)
    logfile.write(strings.BEST_AI_RESULT % (str(top_plays), '\n'))
    strings.send_text(strings.BEST_AI_RESULT % (str(top_plays), ''))
    logfile.close()
