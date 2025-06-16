import random
while True:
    print('''-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Введите диапазон чисел.
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+''')
    a = int(input('Минимум: '))
    b = int(input('Максимум: '))
    rand = random.randint(a,b)
    space = ' '* int(((7 - len(str(rand))) / 2))
    if (len(str(rand)) % 2) == 0:
        space_1 = ' '
    else:
        space_1 = ''
    print(f'''-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
рандом считает:
 _______
|       |
|{space}{rand}{space}{space_1}|
|       |
 ‾‾‾‾‾‾‾''')