from random import randint

def help():
    print('''������ �������:
    q - �����,
    h - ��� ������,
    s - ���������� � ����� �������,
    w - ����� ��������� ����,
    gw - ����� ������ � ����, ��������� 1 ���,
    rw - ������� ������, ��������� 1 ���,
    b - ������ �����,
    s - ������� �����''')

def stat():
    global date, wealth, credit, percent, price, goody_qty
    print('����: %d' % date)
    print('� ��� %d �����' % wealth)
    print('��� ����: %d �����' % credit)
    print('�������� �� �����: %d' % percent)
    print('���� ������: %d' % price)
    print('���������� ������: %d' % goody_qty)

date = 0
wealth = 0
credit = 0
percent = 0
price = 1
goody_qty = 0

def ontime():
    global date, credit, percent, price
    date += 1
    credit = int(credit * (100 + percent) / 100)
    percent += randint(-5, 5)
    price += randint(-3, 3)
    if percent < 0:
        percent = 0
    if price < 1:
        price = 1
    stat()

exit = False
while not exit:
    command = input('you@yourbussiness> ')
    if command == 'q':
        exit = True
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
            print('������������ �����!')
            continue
        wealth -= 1
        credit -= 1
        ontime()
    elif command == 'b':
        if wealth < price:
            print('������������ �����!')
            continue
        wealth -= price
        goody_qty +  1
        ontime()
            
    else:
        print('������� �� �������')
