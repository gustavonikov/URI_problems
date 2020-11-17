N = int(input())

for lines in range(N):
    T = int(input())

    difference = 2014 - T

    if difference < 0:
        print(f'{abs(difference)} A.C.')
    else:
        difference += 1
        print(f'{difference} D.C.')