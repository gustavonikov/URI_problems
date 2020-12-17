while True:
    try:
        dodoChoice, leoChoice, pepperChoice = input().split()

        if dodoChoice == 'pedra' and leoChoice == 'tesoura' and pepperChoice == 'tesoura':
            print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
        elif dodoChoice == 'papel' and leoChoice == 'pedra' and pepperChoice == 'pedra':
            print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
        elif dodoChoice == 'tesoura' and leoChoice == 'papel' and pepperChoice == 'papel':
            print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
        elif leoChoice == 'pedra' and dodoChoice == 'tesoura' and pepperChoice == 'tesoura':
            print("Iron Maiden's gonna get you, no matter how far!")
        elif leoChoice == 'papel' and dodoChoice == 'pedra' and pepperChoice == 'pedra':
            print("Iron Maiden's gonna get you, no matter how far!")
        elif leoChoice == 'tesoura' and dodoChoice == 'papel' and pepperChoice == 'papel':
            print("Iron Maiden's gonna get you, no matter how far!")
        elif pepperChoice == 'pedra' and dodoChoice == 'tesoura' and leoChoice == 'tesoura':
            print('Urano perdeu algo muito precioso...')
        elif pepperChoice == 'papel' and dodoChoice == 'pedra' and leoChoice == 'pedra':
            print('Urano perdeu algo muito precioso...')
        elif pepperChoice == 'tesoura' and dodoChoice == 'papel' and leoChoice == 'papel':
            print('Urano perdeu algo muito precioso...')
        elif (dodoChoice == 'pedra' and leoChoice == 'tesoura' and pepperChoice == 'papel')\
        or (leoChoice == 'pedra' and dodoChoice == 'tesoura' and pepperChoice == 'papel')\
        or (pepperChoice == 'pedra' and dodoChoice == 'tesoura' and leoChoice == 'papel')\
        or (pepperChoice == 'tesoura' and dodoChoice == 'pedra' and leoChoice == 'papel')\
        or (pepperChoice == 'tesoura' and dodoChoice == 'papel' and leoChoice == 'pedra')\
        or (pepperChoice == 'pedra' and dodoChoice == 'papel' and leoChoice == 'tesoura')\
        or (dodoChoice == 'pedra' and leoChoice == 'pedra' and pepperChoice == 'tesoura')\
        or (dodoChoice == 'pedra' and leoChoice == 'pedra' and pepperChoice == 'pedra')\
        or (dodoChoice == 'papel' and leoChoice == 'papel' and pepperChoice == 'pedra')\
        or (dodoChoice == 'papel' and leoChoice == 'papel' and pepperChoice == 'papel')\
        or (dodoChoice == 'tesoura' and leoChoice == 'tesoura' and pepperChoice == 'papel')\
        or (dodoChoice == 'tesoura' and leoChoice == 'tesoura' and pepperChoice == 'tesoura')\
        or (leoChoice == 'pedra' and dodoChoice == 'pedra' and pepperChoice == 'tesoura')\
        or (leoChoice == 'pedra' and dodoChoice == 'pedra' and pepperChoice == 'pedra')\
        or (leoChoice == 'papel' and dodoChoice == 'papel' and pepperChoice == 'pedra')\
        or (leoChoice == 'papel' and dodoChoice == 'papel' and pepperChoice == 'papel')\
        or (leoChoice == 'tesoura' and dodoChoice == 'tesoura' and pepperChoice == 'papel')\
        or (leoChoice == 'tesoura' and dodoChoice == 'tesoura' and pepperChoice == 'tesoura')\
        or (pepperChoice == 'pedra' and dodoChoice == 'pedra' and leoChoice == 'tesoura')\
        or (pepperChoice == 'pedra' and dodoChoice == 'pedra' and leoChoice == 'pedra')\
        or (pepperChoice == 'papel' and dodoChoice == 'papel' and leoChoice == 'pedra')\
        or (pepperChoice == 'papel' and dodoChoice == 'papel' and leoChoice == 'papel')\
        or (pepperChoice == 'tesoura' and dodoChoice == 'tesoura' and leoChoice == 'papel')\
        or (pepperChoice == 'tesoura' and dodoChoice == 'tesoura' and leoChoice == 'tesoura')\
        or (leoChoice == 'papel' and pepperChoice == 'papel' and dodoChoice == 'pedra')\
        or (leoChoice == 'tesoura' and pepperChoice == 'tesoura' and dodoChoice == 'papel')\
        or (leoChoice == 'pedra' and pepperChoice == 'pedra' and dodoChoice == 'tesoura'):
            print('Putz vei, o Leo ta demorando muito pra jogar...') 
        
    except EOFError:
        break