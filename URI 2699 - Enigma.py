# Fazer um array com cada indice sendo uma letra, e ir alterando cada letra que
""" é uma interrogação, pra conferir se a letra já era um número só checar no infos
se o indice a ser alterado tá contido nele. Dá um join no array pra virar string e
dps virar um numero, checando se o número é igual à D
E torcer pra dá certo. """

D, N = input().split()
lenOfD = len(D)
N = int(N)

lowerD = ''
higherD = ''
infos = {}

for index, letter in enumerate(D):
    if letter.isdigit():
        lowerD += letter
        higherD += letter
        infos[index] = letter
    else:
        if index == 0:
            lowerD += '1'
            higherD += '9'
        else:
            lowerD += '0'
            higherD += '9'

lowerD = int(lowerD)
higherD = int(higherD)

rest = lowerD % N
quotient = lowerD // N

if rest != 0:
    while True:
        result = quotient * N
        resultString = str(result)

        matchInfo = 0

        newRest = result % N

        if newRest == 0:
            for position, value in infos.items():
                if resultString[position] == value:
                    matchInfo += 1
                    
        quotient += 1
        
        if result > higherD:
            print('*')
            break
        if len(infos) == matchInfo:
            print(result)
            break
else:
    print(lowerD)