while True:
    try:
        Xf, Yf, Xi, Yi, Vi, R1, R2 = input().split()

        Xf, Yf = int(Xf), int(Yf)
        Xi, Yi = int(Xi), int(Yi)
        targetSpeed = int(Vi)
        ultimateRadius = int(R1)
        crowsRadius = int(R2)

        attackRange = ultimateRadius + crowsRadius
        
        diffPosition = ((Xi - Xf)**2 + (Yi - Yf)**2)**(1/2) + (targetSpeed * 1.5)
        print('Y') if attackRange >= diffPosition else print('N')
        
    except EOFError:
        break
