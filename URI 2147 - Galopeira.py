C = int(input())

for cases in range(C):
    word = input()

    numberOfLetters = len(word)
    result = numberOfLetters * 0.01

    print('%.2f'%result)