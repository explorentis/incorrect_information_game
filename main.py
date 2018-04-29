# -*- coding: utf-8 -*-
from world import World
from company import Company

def help():
    print('''Список комманд:
    q - выход,
    h - эта помощь,
    s - информация о Вашем бизнесе,
    w - ждать следующей даты,
    gw - взять деньги в долг, требуется 1 ход,
    rw - вернуть деньги, требуется 1 ход,
    b - купить товар,
    d - продать товар''')

def player_command():
    return input('you@yourbussiness> ')

world = World(Company(player_command))

aicmd = ['w', 'gw', 'rw', 'b', 'd']

while not world.quit:
    command = world.company.get_command()
    if command == 'q':
        world.quit = True
    elif command == 'h':
        help()
    elif command == 's':
        world.info()
    elif command == 'w':
        world.ontime()
    elif command == 'gw':
        world.company.money += 1
        world.company.credit += 1
        print('test')
        world.ontime()
    elif command == 'rw':
        if world.company.money < 1:
            print('Недостаточно денег!')
            continue
        world.company.money -= 1
        world.company.credit -= 1
        world.ontime()
    elif command == 'b':
        if world.company.money < world.price:
            print('Недостаточно денег!')
            continue
        world.company.money -= world.price
        world.company.goody += 1
        world.ontime()
    elif command == 'd':
        count = 0
        sell_price = 0
        while (choice('yn') == 'y') and (world.company.goody > 0):
            world.company.goody -= 1
            sell_price = int(world.price * 1.2) + 1
            world.company.money += sell_price
            count += 1
        print("Вы продали %d товаров по цене %d" % (count, sell_price))
        world.ontime()
    else:
        print('Команда не найдена')
