huguinho_age, zezinho_age, luisinho_age = input().split()

ages = [huguinho_age, zezinho_age, luisinho_age]

ages.sort()

middle_age = ages[1]

if middle_age == huguinho_age:
  print('huguinho')
elif middle_age == zezinho_age:
  print('zezinho')
elif middle_age == luisinho_age:
  print('luisinho')
