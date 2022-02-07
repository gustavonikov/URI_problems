import math

def primefactors(n):
    while n % 2 == 0:
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while (n % i == 0):
            n = n / i
            return i
    
    if n > 2:
        return n

while True:
    k, l = input().split()
    k, l = int(k), int(l)

    if k == 0 and l == 0:
        break
    
    result = primefactors(k)
    
    if result and l > result:
        print(f'BAD {result}')
    else:
        print('GOOD')
        