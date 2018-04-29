from random import randint, choice

def chkwin():
    if (wealth > 100) and (credit == 0):
        print("Вы выиграли!")
        exit(0)

def chklose():
    if (credit == 100):
        print("Вы проиграли!")
        exit(1)

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

def stat():
    global date, wealth, credit, percent, price, goody_qty
    print('Дата: %d' % date)
    print('У Вас %d денег' % wealth)
    print('Ваш долг: %d денег' % credit)
    print('Проценты по долгу: %d' % percent)
    print('Цена товара: %d' % price)
    print('Количество товара: %d' % goody_qty)

date = 0
wealth = 0
credit = 0
percent = 0
price = 1
goody_qty = 0

def ontime():
    global date, credit, percent, price
    # меняется дата
    date += 1
    # увеличение долга по кредиту
    credit = int(credit * (100 + percent) / 100)
    # изменение процентов по кредиту в этом ходу
    percent += randint(-5, 5)
    # изменение стоимости товаров в этом ходу
    price += randint(-3, 3)
    if percent < 0:
        percent = 0
    if price < 1:
        price = 1
    stat()
    # проверка условий победы и поражения
    chkwin()
    chklose()

quit = False
while not quit:
    command = input('you@yourbussiness> ')
    if command == 'q':
        quit = True
    elif command == 'h':
        help()
    elif command == 's':
        stat()
    elif command == 'w':
        ontime()
    elif command == 'gw':
        wealth += 1
        credit += 1
        ontime()
    elif command == 'rw':
        if wealth < 1:
            print('Недостаточно денег!')
            continue
        wealth -= 1
        credit -= 1
        ontime()
    elif command == 'b':
        if wealth < price:
            print('Недостаточно денег!')
            continue
        wealth -= price
        goody_qty += 1
        ontime()
    elif command == 'd':
        count = 0
        sell_price = 0
        while (choice('yn') == 'y') and (goody_qty > 0):
            goody_qty -= 1
            sell_price = int(price * 1.2) + 1
            wealth += sell_price
            count += 1
        print("Вы продали %d товаров по цене %d" % (count, sell_price))
        ontime()
    else:
        print('Команда не найдена')
