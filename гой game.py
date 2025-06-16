goi = 0
nagret_goev = 1
buy_update = 100


def taptap(goev):
    while True:
        interact1 = input('Enter - нагреть гоев [enter / exit] ')
        
        if interact1 != '':
            break
        else:
            print(f'''
--------------------------------
У вас {goev} гоев


''')
            goev += nagret_goev
    return goev

while True:
    print('''
--------------------------------
|[1] - Нагревать гоев          |
|[2] - Улутшить прогрев гоев   |
|[3] - завершить игру          |
--------------------------------''')
    
    print(f'У вас {goi} гоев')
    choce = input('Что вы хотите сделать?')
    print('')
    
    if choce == '1':
        
        goi = taptap(goi)
    
    if choce == '2':
        
        print(f'Улутшить нагрев стоит: {buy_update} гоев')
        interact = input('Улутшить? [да / нет] ')
        if interact == 'да' and goi >= buy_update:
            nagret_goev += 1
            goi = goi - buy_update
            buy_update = buy_update * 2
            print('Нагрев улутшен')
        elif interact == 'да' and goi < buy_update:
            print('Недостатачно гоев')
    
    if choce == '3':
        
        print('Для завершения игры нужно 1000 гоев')
        interact1 = input('Завершить игру? [да / нет] ')
        if interact1 == 'да' and goi >= 1000:
            print('ИГРА ЗАВЕРШЕНА')
        break