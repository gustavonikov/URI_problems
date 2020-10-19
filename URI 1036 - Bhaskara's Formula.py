coefficients = input().split()

A, B, C = coefficients

def Bhaskara(val1, val2, val3): 
    delta = val2**2 - 4*val1*val3

    if delta < 0 or val1 == 0:
        return print('Impossivel calcular') 
    else:
        R1 = (-val2 + delta**0.5)/(2*val1)
        R2 = (-val2 - delta**0.5)/(2*val1)
        
        return print('R1 = %.5f'%R1), print('R2 = %.5f'%R2)

Bhaskara(float(A), float(B), float(C))