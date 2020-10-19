number = float(input())

intervals = [[0,25],[25,50],[50,75],[75,100]]

if number < 0 or number > 100:
    
    print('Fora de intervalo')
    
elif number >= 0 and number <= 25:
    
    print('Intervalo [0,25]')
    
else:
    
    for interval in intervals:
        
        if number > interval[0] and number <= interval[1]:
            
            print('Intervalo (%i,%i]'%(interval[0], interval[1]))
