D = int(input())

score = 0

if D <= 800:
    score = 1
elif D <= 1400:
    score = 2
elif D <= 2000:
    score = 3

print(score)