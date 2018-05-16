# -*- coding: utf-8 -*-
# Copyright © 2018 Sergei Kuznetsov. All rights reserved.


class Director:
    def __init__(self, command_function, parameters=None):
        # credit_sum=85, money_for_product_reserve=11):

        self.command = command_function
        self.company = None
        self.last_command = None
        #
        if parameters is None:
            self.parameters = {'credit_sum': 85,
                               'money_for_product_reserve': 11}
        else:
            self.parameters = parameters.copy()

    def get_command(self):
        self.last_command = self.command(self)
