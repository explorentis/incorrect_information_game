# -*- coding: utf-8 -*-
from random import randint

class World:
    def __init__(self, companies):
        self.date = 0
        self.percent = 0
        self.price = 1
        self.companies = companies
        self.quit = False
    
    def info(self, forced=False):
        print('Дата: %d' % self.date)
        print('Проценты по долгу: %d' % self.percent)
        print('Цена товара: %d' % self.price)
        for c in self.companies:
            c.info(forced)
        
    def ontime(self):
        # меняется дата
        self.date += 1
        # увеличение долга по кредиту
        for c in self.companies:
            c.credit = int(c.credit * (100 + self.percent) / 100)
        # изменение процентов по кредиту в этом ходу
        self.percent += randint(-5, 5)
        # изменение стоимости товаров в этом ходу
        self.price += randint(-3, 3)
        if self.percent < 0:
            self.percent = 0
        if self.price < 1:
            self.price = 1
        self.info()
        # проверка условий победы и поражения
        self.chkwin()
        self.chklose()
    
    def chkwin(self):
        for c in self.companies:
            if (c.money > 100) and (c.credit == 0) and (c.show_messages):
                print("%s: Вы выиграли!" % c.name)
                self.quit = True

    def chklose(self):
        for c in self.companies:
            if (c.credit == 100) and (c.show_messages):
                print("%s: Вы проиграли!" % c.name)
                self.quit = True
