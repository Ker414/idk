import random
import time
import os

warrior = [0,1,2,3,4,5,6,7,8]
random.shuffle(warrior)

board =['[ ]','[ ]','[ ]',
        '[ ]','[ ]','[ ]',
        '[ ]','[ ]','[ ]']
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def warrior_chose():
    if board[warrior[0]] == '[ ]':
        board[warrior[0]] = ' O '
        warrior.pop(0)
    else:
        warrior.pop(0)
        warrior_chose()
def turn_player():
    turn = int(input('Выберете клетку: ')) - 1
    if board[turn] == '[ ]':
        board[turn] = ' x '
    else:
        print('Клетка занята, выберете другую')
        turn_player()
    
    clear_terminal()
    
    print(f'''Ваш ход:
{board[0]} {board[1]} {board[2]}
{board[3]} {board[4]} {board[5]}
{board[6]} {board[7]} {board[8]}''')
    
    time.sleep(1)
    clear_terminal()

print(f'''{board[0]} {board[1]} {board[2]}
{board[3]} {board[4]} {board[5]}
{board[6]} {board[7]} {board[8]}''')

while True:
    turn_player()
    
    if board[0] == ' x ' and board[1] == ' x ' and board[2] == ' x ':
        print('Игрок выиграл')
        break
    if board[3] == ' x ' and board[4] == ' x ' and board[5] == ' x ':
        print('Игрок выиграл')
        break
    if board[6] == ' x ' and board[7] == ' x ' and board[8] == ' x ':
        print('Игрок выиграл')
        break
    if board[0] == ' x ' and board[3] == ' x ' and board[6] == ' x ':
        print('Игрок выиграл')
        break
    if board[1] == ' x ' and board[4] == ' x ' and board[7] == ' x ':
        print('Игрок выиграл')
        break
    if board[2] == ' x ' and board[5] == ' x ' and board[8] == ' x ':
        print('Игрок выиграл')
        break
    if board[0] == ' x ' and board[4] == ' x ' and board[8] == ' x ':
        print('Игрок выиграл')
        break
    if board[2] == ' x ' and board[4] == ' x ' and board[6] == ' x ':
        print('Игрок выиграл')
        break
    
    warrior_chose()
    print(f'''Ход врага:
{board[0]} {board[1]} {board[2]}
{board[3]} {board[4]} {board[5]}
{board[6]} {board[7]} {board[8]}''',)
    
    if board[0] == ' O ' and board[1] == ' O ' and board[2] == ' O ':
        print('Бот выиграл')
        break
    if board[3] == ' O ' and board[4] == ' O ' and board[5] == ' O ':
        print('Бот выиграл')
        break
    if board[6] == ' O ' and board[7] == ' O ' and board[8] == ' O ':
        print('Бот выиграл')
        break
    if board[0] == ' O ' and board[3] == ' O ' and board[6] == ' O ':
        print('Бот выиграл')
        break
    if board[1] == ' O ' and board[4] == ' O ' and board[7] == ' O ':
        print('Бот выиграл')
        break
    if board[2] == ' O ' and board[5] == ' O ' and board[8] == ' O ':
        print('Бот выиграл')
        break
    if board[0] == ' O ' and board[4] == ' O ' and board[8] == ' O ':
        print('Бот выиграл')
        break
    if board[2] == ' O ' and board[4] == ' O ' and board[6] == ' O ':
        print('Бот выиграл')
        break