# -*- coding: utf-8 -*-
class Company:
    def __init__(self, control):
        self.money = 0
        self.credit = 0
        self.goody = 0
        # Указатель на функцию, возвращающую выбранное действие
        self.get_command = control
    
    def info(self):
        print('У Вас %d денег' % self.money)
        print('Ваш долг: %d денег' % self.credit)
        print('Количество товара: %d' % self.goody)
