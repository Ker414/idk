while True:
    print('Введите слово или несколько')
    word = input()
    reversed_word = ''
    split_word = list(word)
    for i in range(len(word)):
        reversed_word = reversed_word + split_word.pop()
    print(reversed_word)