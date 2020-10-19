inputedSalary = float(input())

def Taxes(salary):
    adjustedSalary = salary - 2000.00
    adjustedSalary2 = salary - 3000.00
    adjustedSalary3 = salary - 4500.00
    
    if salary >= 2000.01 and salary <= 3000.00:
        tax = adjustedSalary * 0.08
    
    elif salary >= 3000.01 and salary <= 4500.00:
        tax = (adjustedSalary - adjustedSalary2) * 0.08 + adjustedSalary2 * 0.18
        
    elif salary > 4500.00:
        tax = (adjustedSalary - adjustedSalary2) * 0.08 + (adjustedSalary2 - adjustedSalary3) * 0.18 + adjustedSalary3 * 0.28
        
    return print('R$ %.2f'%tax)

if inputedSalary >= 0.00 and inputedSalary <= 2000.00:
    print('Isento')
    
else:
    Taxes(inputedSalary)