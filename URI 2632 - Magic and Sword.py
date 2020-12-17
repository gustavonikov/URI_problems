T = int(input())

for cases in range(T):
    w, h, x0, y0 = input().split()
    spell, N, cx, cy = input().split()
    
    w, h, x0, y0 = int(w), int(h), int(x0), int(y0)
    cx, cy = int(cx), int(cy)

    x1 = w + x0
    y1 = h + y0

    if spell == 'fire':
        power = 200
        if N == '1':
            spellRange = 20
        elif N == '2':
            spellRange = 30
        elif N == '3':
            spellRange = 50
    elif spell == 'water':
        power = 300
        if N == '1':
            spellRange = 10
        elif N == '2':
            spellRange = 25
        elif N == '3':
            spellRange = 40
    elif spell == 'earth':
        power = 400
        if N == '1':
            spellRange = 25
        elif N == '2':
            spellRange = 55
        elif N == '3':
            spellRange = 70
    elif spell == 'air':
        power = 100
        if N == '1':
            spellRange = 18
        elif N == '2':
            spellRange = 38
        elif N == '3':
            spellRange = 60
    
    if cx > x1:
        if cy > y1:
            diff = ((x1 - cx)**2 + (y1 - cy)**2)**(1/2)
        elif cy < y0:
            diff = ((x1 - cx)**2 + (y0 - cy)**2)**(1/2)
        elif y0 <= cy <= y1:
            diff = ((x1 - cx)**2)**(1/2)
    elif cx < x0:
        if cy > y1:
            diff = ((x0 - cx)**2 + (y1 - cy)**2)**(1/2)
        elif cy < y0:
            diff = ((x0 - cx)**2 + (y0 - cy)**2)**(1/2)
        elif y0 <= cy <= y1:
            diff = ((x0 - cx)**2)**(1/2)
    elif x0 <= cx <= x1:
        if cy > y1:
            diff = ((y1 - cy)**2)**(1/2)
        elif cy < y0:
            diff = ((y0 - cy)**2)**(1/2)
        elif y0 <= cy <= y1:
            diff = 0
    
    if spellRange >= diff:
        print(power)
    else:
        print(0)
