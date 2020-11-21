import math

n = int(input())

minimum = n/math.log(n)
maximum = 1.25506 * (n/math.log(n))

print('%.1f %.1f'%(minimum, maximum))