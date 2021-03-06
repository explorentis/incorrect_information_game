# -*- coding: utf-8 -*-
# Copyright © 2018 Sergei Kuznetsov. All rights reserved.
from random import randint

import strings


class World:
    def __init__(self, companies, hideoutput=False):
        self.winner_is_here = False
        self.date = 0
        self.percent = 0
        self.price = 1
        self.companies = companies
        self.hideoutput = hideoutput
        for c in self.companies:
            c.world = self
        self.quit = False

    def info(self, forced=False):
        if not self.hideoutput:
            strings.send_text(strings.DATE % self.date)
            strings.send_text(strings.CREDIT_PERCENT % self.percent)
            strings.send_text(strings.PRODUCT_PRICE % self.price)
        for c in self.companies:
            c.info(forced)

    def ontime(self):
        # меняется дата
        self.date += 1
        # увеличение долга по кредиту
        for c in self.companies:
            c.credit = int(c.credit * (100 + self.percent) / 100)
            # Трата на еду:
            if c.money > self.price:
                c.money -= self.price
            else:
                c.credit += self.price
            # .
        self.increase_credit_percent(randint(-5, 5))
        self.increase_product_price(randint(-3, 3))
        self.info()
        # проверка условий победы и поражения
        self.chkwin()
        self.chklose()

    # изменение процентов по кредиту в этом ходу
    def increase_credit_percent(self, value):
        self.percent += value
        if self.percent < 0:
            self.percent = 0

    def increase_product_price(self, value):
        # изменение стоимости товаров в этом ходу
        self.price += value
        if self.price < 1:
            self.price = 1

    def chkwin(self):
        for c in self.companies:
            if (c.money > 100) and (c.credit == 0):
                if (c.show_messages):
                    strings.send_text(strings.WIN % c.name)
                self.winner_is_here = True
                self.quit = True

    def chklose(self):
        for c in self.companies:
            if c.credit > 100:
                if c.show_messages:
                    strings.send_text(strings.LOSE % c.name)
                self.winner_is_here = False
                self.quit = True
