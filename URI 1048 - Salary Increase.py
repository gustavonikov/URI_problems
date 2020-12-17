currentSalary = float(input())

salaries = [[0.00,400.00],[400.01,800.00],[800.01, 1200.00],[1200.01, 2000.00]]
readjustRate = [0.15, 0.12, 0.1, 0.07]

if currentSalary > 2000.00:
    moneyEarned = currentSalary * 0.04
    newSalary = currentSalary + moneyEarned
    readjust = 4 

    print('Novo salario: %.2f'%newSalary)
    print('Reajuste ganho: %.2f'%moneyEarned)
    print('Em percentual: ' + str(readjust) + ' %')

else:
    for salary in salaries:
        if currentSalary >= salary[0] and currentSalary <= salary[1]:
            moneyEarned = currentSalary * readjustRate[salaries.index(salary)]
            newSalary = currentSalary + moneyEarned
            readjust = int(readjustRate[salaries.index(salary)] * 100)

            print('Novo salario: %.2f'%newSalary)
            print('Reajuste ganho: %.2f'%moneyEarned)
            print('Em percentual: ' + str(readjust) + ' %')