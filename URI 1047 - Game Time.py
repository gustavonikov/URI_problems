x = input().split()

hi = int(x[0])
mi = int(x[1])
hf = int(x[2])
mf = int(x[3])

if(hi == hf) & (mi == mf):
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')

else:
    hora = hf - hi
    minuto = mf - mi

    if(hora < 0):
        hora += 24
        
    if(minuto < 0):
        minuto += 60
        hora -= 1
    
    print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)' %(hora, minuto))