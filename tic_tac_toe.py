# Autor: Andrei Reshetniak
# License: GNU GPL v. 3
# 2018

def branch_1(cell):
    print('Отладочная информация: переход на ветку 1.')
    print ("Ход машины: клетка 2.")
    print ("Ваш ход: Ведите номер клетки   и нажмите Ввод  (Enter)")
    cell = int(input())
    if cell == 6:
        print ("Ход человека: клетка 6.")
        print ("Ход машины: клетка 7.")
        print ("Ваш ход: Ведите номер клетки   и нажмите Ввод (Enter)")
        cell = int(input())
        if cell == 3:
            print ("Ход человека: клетка 3.")
            print ("Ход машины: клетка 8.")
            print ("Ваш ход: Ведите номер клетки   и нажмите Ввод (Enter)")
            cell = int(input())
            if cell == 4:
                print ("Ход человека: клетка 4.")
                print ('Ход машины: клетка 5.')
                print('Конец игры!Ничья!')
                exit()
            else:
                print ('4')
                print('Конец игры!Победила машина!')
                exit()
        else:
            print ('3')
            print('Конец игры!Победила машина!')
            exit()
    else:
        print ('6')
        print('Конец игры!Победила машина!')
        exit()


def branch_2(cell):
    print('Отладочная информация: переход на ветку 2.')
    print ("Ход машины: клетка 2.")
    print ("Ваш ход: Ведите номер клетки   и нажмите Ввод (Enter)")
    cell = int(input())
    if cell == 6:
        print ("Ход человека: клетка 6.")
        print ("Ход машины: клетка 5.")
        print ("Ваш ход: Ведите номер клетки   и нажмите Ввод (Enter)")
        cell = int(input())
        if cell == 1:
            print ("Ход человека: клетка 1.")
            print('Ход машины: клетка 8.')
            cell = int(input())
            if cell == 4:
                print('Ход машины: клетка 7.')
                print('Конец игры!Ничья!')
                exit()
            else:
                print('4')
                exit()
        else:
            print('1')
            exit()
    else:
        print ('6')
        print('Конец игры!Победила машина!')
        exit()


def branch_3(cell):
    print('Отладочная информация: переход на ветку 3.')
    print('Ход машины: клетка 6.')
    print ("Ваш ход: Ведите номер клетки   и нажмите Ввод (Enter)")
    cell = int(input())
    if cell == 2:
        print('Ход человека: клетка 2.')
        print ("Ход машины: клетка 3.")
        print ("Ваш ход: Ведите номер клетки   и нажмите Ввод (Enter)")
        cell = int(input())
        if cell == 7:
            print('Ход человека: клетка 7.')
            print ("Ход машины: клетка 8.")
            print ("Ваш ход: Ведите номер клетки   и нажмите Ввод (Enter)")
            cell = int(input())
            if cell == 4:
                print('Ход человека: клетка 4.')
                print('Ход машины: клетка 1.')
                print('Конец игры!Ничья!')
                exit()
            else:
                print('4')
                print('Конец игры!Победила машина!')
                exit()
        else:
            print('7')
            print('Конец игры!Победила машина!')
            exit()
    else:
        print('6')
        print('Конец игры!Победила машина!')
        exit()

def branch_4(cell):
    print('Отладочная информация: переход на ветку 4.')
    print('Ход машины: клетка 6.')
    print('Ваш ход: Ведите номер клетки   и нажмите Ввод (Enter)')
    cell = int(input())
    if cell == 2:
        print('Ход человека: клетка 2.')
        print('Ход машины: клетка 1.')
        print('Ваш ход: Ведите номер клетки   и нажмите Ввод (Enter)')
        cell = int(input())
        if cell == 5:
            print('Ход человека: клетка 5')
            print('Ход машины: клетка 8')
            print('Ваш ход: Ведите номер клетки   и нажмите Ввод (Enter)')
            cell = int(input())
            if cell == 4:
                print('Ход человека: клетка 4')
                print('Ход машины: клетка 3')
                print('Конец игры!Ничья!')
                exit()
            else:
                 print('4')
                 print('Конец игры!Победила машина!')
                 exit()
        else:
            print('5')
            print('Конец игры!Победила машина!')
            exit()
    else:
        print('2')
        print('Конец игры!Победила машина!')
        exit()


def branch_5(cell):
    print('Отладочная информация: переход на ветку 5.')
    print('Ход машины: клетка 7.')
    print('Ваш ход: Ведите номер клетки   и нажмите Ввод (Enter)')
    cell = int(input())
    if cell == 3:
        print('Ход человека: клетка 3')
        print('Ход машины: клетка 5')
        print('Конец игры!Победила машина!')
        exit()
    else:
        print('3')
        print('Конец игры!Победила машина!')
        exit()

def branch_6(cell):
    print('Отладочная информация: переход на ветку 6.')
    print('Ход машины: клетка 7.')
    print('Ваш ход: Ведите номер клетки   и нажмите Ввод (Enter)')
    cell = int(input())
    if cell == 3:
        print('Ход человека: клетка 3')
        print('Ход машины: клетка 1')
        print('Конец игры!Победила машина!')
        exit()
    else:
        print('3')
        print('Конец игры!Победила машина!')
        exit()

def branch_7(cell):
    print('Отладочная информация: переход на ветку 7.')
    print('Ход машины: клетка 3.')
    print('Ваш ход: Ведите номер клетки   и нажмите Ввод (Enter)')
    cell = int(input())
    if cell == 7:
        print('Ход человека: клетка 7')
        print('Ход машины: клетка 1')
        print('Конец игры!Победила машина!')
        exit()
    else:
        print('7')
        print('Конец игры!Победила машина!')
        exit()

def branch_8(cell):
    print('Отладочная информация: переход на ветку 8.')

print ("Ход машины: клетка 9.")
print ("Ваш ход: Ведите номер клетки и нажмите Ввод (Enter)")
cell = int(input())
if cell == 1:
    branch_1(cell)
if cell == 3:
    branch_2(cell)
if cell == 5:
    branch_3(cell)
if cell == 7:
    branch_4(cell)
if cell == 8:
    branch_5(cell)
if cell == 6:
    branch_6(cell)
if cell == 4:
    branch_7(cell)
if cell == 2:
    branch_8(cell)
