message = input()

countOne = 0

for letter in message:
    if letter == '1':
        countOne += 1

if countOne % 2 != 0:
    message += '1'
else:
    message += '0'

print(message)