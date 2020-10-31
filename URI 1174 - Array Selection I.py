A = []

for value in range(0, 100):
    A.append(input())

for index, number in enumerate(A):
    number = float(number)
    if number <= 10:
        print('A[%i] = %.1f'%(index, number))
