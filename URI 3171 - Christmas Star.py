from datetime import date, timedelta
import math

initialDate = date(2020, 12, 21)

N = int(input())

earthDays = N * 365.25

jupiterDays = earthDays * 11.9
jupiterDays = math.floor(jupiterDays)
jupiterDate = initialDate + timedelta(jupiterDays)

saturnDays = earthDays * 29.6
saturnDays = math.floor(saturnDays)
saturnDate = initialDate + timedelta(saturnDays)

print(f'Dias terrestres para Jupiter = {jupiterDays}')
print(f'Data terrestre para Jupiter: {jupiterDate}')
print(f'Dias terrestres para Saturno = {saturnDays}')
print(f'Data terrestre para Saturno: {saturnDate}')