N = int(input())

inside, out = 0, 0

for number in range(N):
    X = int(input())
    if X >= 10 and X <= 20:
        inside += 1
    else:
        out += 1

print(inside,'in')
print(out,'out')
