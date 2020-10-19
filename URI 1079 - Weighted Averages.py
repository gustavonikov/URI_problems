N = int(input())

numbers = []

for number in range(N):
    val1, val2, val3 = input().split()
    
    weightedAverage = (float(val1) * 2 + float(val2) * 3 + float(val3) * 5)/(10)
    
    numbers.append(weightedAverage)

for number in numbers:
    print('%.1f'%number)