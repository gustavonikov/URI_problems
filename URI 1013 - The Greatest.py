values = input().split()

a = int(values[0])
b = int(values[1])
c = int(values[2])

greatestAB = (a+b+abs(a-b))/2
greatestBC = (b+c+abs(b-c))/2

if greatestAB == b and greatestBC == c:
    print('%i eh o maior'%(greatestBC))
elif greatestAB == a and greatestBC == c:
    greatestAC = (a+c+abs(a-c))/2
    print('%i eh o maior'%(greatestAC))
elif greatestAB == b and greatestBC == b:
    print('%i eh o maior'%(b))
elif greatestAB == a and greatestBC == b:
    print('%i eh o maior'%(a))
    
    