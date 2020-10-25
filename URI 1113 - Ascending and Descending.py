password = 2002

while True:
    insertedPassword = int(input())

    if insertedPassword == password: 
        print('Acesso Permitido')
        break
    else:
        print('Senha Invalida')
    
