DDDcode = int(input())

DDDlist = {
  61: 'Brasilia',
  71: 'Salvador',
  11: 'Sao Paulo',
  21: 'Rio de Janeiro',
  32: 'Juiz de Fora',
  19: 'Campinas',
  27: 'Vitoria',
  31: 'Belo Horizonte',
}

if DDDcode in DDDlist:
    for DDD, city in DDDlist.items():
        if DDDcode == DDD:
            print(city)
            
else:
    print('DDD nao cadastrado')
    