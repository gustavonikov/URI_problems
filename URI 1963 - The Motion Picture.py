A, B = input().split()
A, B = float(A), float(B)

increase = B - A
percentageIncrease = (increase/A) * 100

print('{:.2f}%'.format(percentageIncrease))
