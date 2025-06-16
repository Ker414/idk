import random
import os
import time

# Очистка терминала
def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

def game_start():
    # Игрок и дилер берут карты
    for i in range(2):
        draw_card = colode.pop()
        player_cards.append(draw_card)
        global player_own_card
        player_own_card += 1
    for i in range(2):
        draw_card = colode.pop()
        dealer_cards.append(draw_card)
    global dealer_show
    dealer_show = False
    
    # Отрисовка
    def Printing():
        if dealer_show is False:
            dealer_show_cards = f''' Карты дилера:
-------   --------
| {dealer_cards[0][0]}{dealer_cards[0][1]} |   |скрыто|
|     |   |      |
|     |   |      |
-------   --------'''
        if dealer_show is True:
            dealer_show_cards = f''' Карты дилера:
-------   -------
| {dealer_cards[0][0]}{dealer_cards[0][1]} |   | {dealer_cards[1][0]}{dealer_cards[1][1]} |
|     |   |     |
|     |   |     |
-------   -------'''
        print(dealer_show_cards)
        print('Ваши карты:')
        i = 0
        for i in range(player_own_card):
            print(f'''-------  
| {player_cards[i][0]}{player_cards[i][1]} |  
|     |  
|     |  
-------''')
    
    Printing()
    
    # Действие
    def doing():
        player_chose = int(input('''Взять карту?
[взять карту (1) ][хватит (2) ]
'''))
        
        if player_chose == 1:
            clear_terminal()
            
            draw_card = colode.pop()
            player_cards.append(draw_card)
            global player_own_card
            player_own_card += 1
            Printing()
            doing()
        
        if player_chose == 2:
            global dealer_show
            clear_terminal()
            
            dealer_show = True
            Printing()
            
            # Подсчёт очков игрока
            player_score = 0
            
            i = 0
            for i in range(player_own_card):
                if player_cards[i][1] == '2 ':
                    player_score += 2
                if player_cards[i][1] == '3 ':
                    player_score += 3
                if player_cards[i][1] == '4 ':
                    player_score += 4
                if player_cards[i][1] == '5 ':
                    player_score += 5
                if player_cards[i][1] == '6 ':
                    player_score += 6
                if player_cards[i][1] == '7 ':
                    player_score += 7
                if player_cards[i][1] == '8 ':
                    player_score += 8
                if player_cards[i][1] == '9 ':
                    player_score += 9
                if player_cards[i][1] == '10':
                    player_score += 10
                if player_cards[i][1] == 'В ':
                    player_score += 10
                if player_cards[i][1] == 'Д ':
                    player_score += 10
                if player_cards[i][1] == 'К ':
                    player_score += 10
            
            # Подсчёт очков с тузов
            TS = 0
            i = 0
            for i in range(player_own_card):
                if player_cards[i][1] == 'Т ':
                    TS += 1
            
            # 1 ТУЗ
            if TS == 1 and (player_score + 11) < 22:
                player_score += 11
            elif TS == 1:
                player_score += 1
            
            # 2 ТУЗА
            if TS == 2 and (player_score + 22) < 22:
                player_score += 22
            elif TS == 2 and (player_score + 12) < 22:
                player_score += 12
            elif TS == 2:
                player_score += 2
            
            # 3 ТУЗА
            if TS == 3 and (player_score + 33) < 22:
                player_score += 33
            elif TS == 3 and (player_score + 23) < 22:
                player_score += 23
            elif TS == 3 and (player_score + 13) < 22:
                player_score += 13
            elif TS == 3 and (player_score + 3) < 22:
                player_score += 3
            
            # 4 ТУЗА
            if TS == 4 and (player_score + 44) < 22:
                player_score += 44
            elif TS == 4 and (player_score + 34) < 22:
                player_score += 34
            elif TS == 4 and (player_score + 24) < 22:
                player_score += 24
            elif TS == 4 and (player_score + 14) < 22:
                player_score += 14
            elif TS == 4 and (player_score + 4) < 22:
                player_score += 4
            
            # Подсчёт очков дилера
            dealer_score = 0
            
            i = 0
            for i in range(2):
                if dealer_cards[i][1] == '2 ':
                    dealer_score += 2
                if dealer_cards[i][1] == '3 ':
                    dealer_score += 3
                if dealer_cards[i][1] == '4 ':
                    dealer_score += 4
                if dealer_cards[i][1] == '5 ':
                    dealer_score += 5
                if dealer_cards[i][1] == '6 ':
                    dealer_score += 6
                if dealer_cards[i][1] == '7 ':
                    dealer_score += 7
                if dealer_cards[i][1] == '8 ':
                    dealer_score += 8
                if dealer_cards[i][1] == '9 ':
                    dealer_score += 9
                if dealer_cards[i][1] == '10':
                    dealer_score += 10
                if dealer_cards[i][1] == 'В ':
                    dealer_score += 10
                if dealer_cards[i][1] == 'Д ':
                    dealer_score += 10
                if dealer_cards[i][1] == 'К ':
                    dealer_score += 10
            
            # Подсчёт очков с тузов
            DTS = 0
            i = 0
            for i in range(2):
                if dealer_cards[i][1] == 'Т ':
                    DTS += 1
            
            # 1 ТУЗ
            if DTS == 1 and (dealer_score + 11) < 22:
                dealer_score += 11
            elif DTS == 1:
                dealer_score += 1
            
            # 2 ТУЗА
            if DTS == 2 and (dealer_score + 22) < 22:
                dealer_score += 22
            elif DTS == 2 and (dealer_score + 12) < 22:
                dealer_score += 12
            elif DTS == 2:
                dealer_score += 2
            
            print('Ваши очки:',player_score)
            print('Очки дилера:',dealer_score)
            
            # ПРОВЕРКА ПОБЕДЫ
            global player_win
            if player_score > 21:
                player_win = False
                print('''


---------------------------
|                         |
|     *дилер победил*     |
|                         |
---------------------------
''')
            elif player_score == dealer_score:
                player_win = False
                print('''


---------------------------
|                         |
|         *ничья*         |
|                         |
---------------------------
''')
            elif dealer_score > player_score:
                player_win = False
                print('''


---------------------------
|                         |
|     *дилер победил*     |
|                         |
---------------------------
''')
            elif player_score > dealer_score:
                player_win = True
                print('''


---------------------------
|                         |
|     *игрок победил*     |
|                         |
---------------------------
''')
    
    doing()

# Старт игры

data = {'money': 10}

while True:
    clear_terminal()
    # Ставка
    print(f'''
------------------------------
время ставки!
ваши фишки: {data["money"]}$
------------------------------''')
    bid = int(input('''Сколько ставим?
'''))
    
    
    data["money"] -= bid
    clear_terminal()
    
    # Создание колоды
    ranks = ['2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10','В ','Д ','К ','Т ']
    suits = ['♠','♣','♥','♦']
    colode = [(suit,rank) for suit in suits for rank in ranks]
    random.shuffle(colode)
    player_cards = []
    dealer_cards = []
    player_own_card = 0
    
    # Проверка банкротства
    if data["money"] < 0:
        print('ВЫ БАНКРОТ')
        time.sleep(2)
        break
    
    # Начало игры
    player_win = False
    
    game_start()
    
    # Проверка ставки
    if player_win is True:
        data["money"] = data["money"] + (bid * 2)
    
    time.sleep(2)