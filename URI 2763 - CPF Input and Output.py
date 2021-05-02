CPFinput = input()
firstPart, secondPart, thirdAndFourthPart = CPFinput.split('.')
thirdPart, fourthPart = thirdAndFourthPart.split('-')

print(f'{firstPart}\n{secondPart}\n{thirdPart}\n{fourthPart}')