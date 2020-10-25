grades = []

while True:
    grade = float(input())

    if grade < 0 or grade > 10:
        print('nota invalida')
    else:
        grades.append(grade)
    
    if len(grades) == 2:
        break

average = sum(grades)/len(grades)
print('media = %.2f'%average)
