A, B, C = input().split()
A, B, C = int(A), int(B), int(C)

happyFace = ':)'
sadFace = ':('

firstToSecondDayDifference = B - A 
secondToThirdDayDifference = C - B

if firstToSecondDayDifference < 0 and secondToThirdDayDifference >= 0:
    print(happyFace)
elif firstToSecondDayDifference > 0 and secondToThirdDayDifference <= 0:
    print(sadFace)
elif firstToSecondDayDifference > 0 and secondToThirdDayDifference > 0 and secondToThirdDayDifference < firstToSecondDayDifference:
    print(sadFace)
elif firstToSecondDayDifference > 0 and secondToThirdDayDifference > 0 and secondToThirdDayDifference >= firstToSecondDayDifference:
    print(happyFace)
elif firstToSecondDayDifference < 0 and secondToThirdDayDifference < 0 and secondToThirdDayDifference > firstToSecondDayDifference:
    print(happyFace)
elif firstToSecondDayDifference < 0 and secondToThirdDayDifference < 0 and secondToThirdDayDifference <= firstToSecondDayDifference:
    print(sadFace)
elif firstToSecondDayDifference == 0 and secondToThirdDayDifference > 0:
    print(happyFace)
elif firstToSecondDayDifference == 0 and secondToThirdDayDifference <= 0:
    print(sadFace)
