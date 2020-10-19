age = int(input())

ageInYears = int(age/365)
ageInMonths = int((age - int(ageInYears * 365))/30)
ageInDays = age - (ageInYears * 365 + ageInMonths * 30)

print('%i ano(s)'%ageInYears)
print('%i mes(es)'%ageInMonths)
print('%i dia(s)'%ageInDays)