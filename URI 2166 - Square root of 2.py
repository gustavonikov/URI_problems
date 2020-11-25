N = int(input())

initialValue = 1.0

values = [value for value in range(N)]

if N == 0:
    print('%.10f'%initialValue)
else:
    increment = 1/2
    for value in values[-1:0:-1]:
        parcel = 1.0/(2.0 + increment)
        increment = parcel
    
    print('%.10f'%(initialValue + increment))