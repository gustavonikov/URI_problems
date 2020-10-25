grades = []

while True:
    while True:
        grade = float(input())

        if grade >= 0 and grade <= 10:
            grades.append(grade)
        else:
            print('nota invalida')
        
        if len(grades) == 2:
            average = sum(grades)/len(grades)
            print('media = %.2f'%average)
            
            break
    
    X = 0
    
    while True:
        X = int(input())
        print('novo calculo (1-sim 2-nao)')

        if X == 1 or X == 2:
            X = X
            break
        else:
            continue
    
    if X == 1:
        grades = []
        continue
    elif X == 2:
        break
    
        
        

