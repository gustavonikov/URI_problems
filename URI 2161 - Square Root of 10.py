N = int(input())

initialValue = 3.0

values = [value for value in range(N)]

if N == 0:
    print('%.10f'%initialValue)
else:
    increment = 1/6
    for value in values[-1:0:-1]:
        parcel = 1.0/(6.0 + increment)
        increment = parcel
    
    print('%.10f'%(initialValue + increment))