import math

a, b = input().split()
a, b = int(a), int(b)

if (a > 0 and b > 0) or (a < 0 and b > 0):
    r = a % b
    q = int((a - r)/b)
elif (a > 0 and b < 0):
    q = int(a/b)
    r = -(b*q) + a
elif  (a < 0 and b < 0):
    q = math.ceil(abs(a) / abs(b))
    r = -(b*q) + a
elif a == 0:
    q, r = 0, 0

print(q, r)
