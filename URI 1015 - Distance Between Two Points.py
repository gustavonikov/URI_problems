point1 = input().split()
point2 = input().split()

x1, y1 = point1
x2, y2 = point2

distance = ((float(x2)-float(x1))**2+(float(y2)-float(y1))**2)**(1/2)

print('%.4f'%(distance))