S, T, F = input().split()
S, T, F = int(S), int(T), int(F)

localTime = S + T + F

if localTime >= 24:
    localTime -= 24
if localTime < 0:
    localTime += 24

print(localTime)
