I = 0.0
J = [1, 2, 3]
count = 0.0
increment = 0.0

while I <= 2:
    for numb in J:
        numb += count
        
        if int(numb) == numb:
            print('I=%i'%I,'J=%i'%numb)

        else: 
            print('I=%.1f'%I,'J=%.1f'%numb)

    I += .2
    I = round(I,1)
    count += .2
