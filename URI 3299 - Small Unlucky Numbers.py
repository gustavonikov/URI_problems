N = input()
has_bad_lucky = False

for index, digit in enumerate(N):
  if index == len(N) - 1:
    break

  if digit == '1' and N[index + 1] == '3':
    print(f'{N} es de Mala Suerte')
    has_bad_lucky = True
    break

if has_bad_lucky == False:
  print(f'{N} NO es de Mala Suerte')
