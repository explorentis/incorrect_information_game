# -*- coding: utf-8 -*-
# Copyright © 2018 Sergei Kuznetsov. All rights reserved.
from random import choice, randint

import strings


def genname():
    def genchar():
        return choice('ЦУКЕНГШЩЗХФВАПРОЛДЖЭЯЧСМИТБЮ')
    return ''.join([genchar() for i in range(0, randint(2, 6))])


class Company:
    def __init__(self, director, show_msg=False):
        # Указатель на мир, которому принадлежит компания (для получения цен и
        # т.д.)
        self.world = None
        self.name = genname()
        self.money = 0
        self.credit = 0
        self.goody = 0
        self.show_messages = show_msg
        # Указатель на функцию, возвращающую выбранное действие
        self.director = director
        self.director.company = self
        # Флаг того, что данная компания сделала свой ход
        self.turn_finished = False

    def info(self, forced=False):
        if self.show_messages or forced:
            strings.send_text(strings.MONEY % (self.name, self.money))
            strings.send_text(strings.CREDIT % (self.name, self.credit))
            strings.send_text(strings.PRODUCTS % (self.name, self.goody))
            strings.send_text(strings.LAST_TURN %
                              (self.name, self.director.last_command))

    def get_command(self):
        self.director.get_command()
