# -*- coding: utf-8 -*-
from random import randint, choice

class World:
    def __init__(self, company):
        self.date = 0
        self.percent = 0
        self.price = 1
        self.company = company
        self.quit = False
    
    def info(self):
        print('Дата: %d' % self.date)
        print('Проценты по долгу: %d' % self.percent)
        print('Цена товара: %d' % self.price)
        self.company.info()
        
    def ontime(self):
        # меняется дата
        self.date += 1
        # увеличение долга по кредиту
        self.company.credit = int(self.company.credit * (100 + self.percent) / 100)
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
        if (self.company.money > 100) and (self.company.credit == 0):
            print("Вы выиграли!")
            self.quit = True

    def chklose(self):
        if (self.company.credit == 100):
            print("Вы проиграли!")
            self.quit = True
