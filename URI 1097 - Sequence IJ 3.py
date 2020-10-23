J = [5, 4, 3]
count = 2

for numbs in range(1,10,2):
    for numb in J:
        numb += count
        print('I=%i'%numbs,'J=%i'%numb)

    count += 2