N = int(input())

numbers = input().split(maxsplit=N)

numbers = [int(number) for number in numbers]
value = max(numbers) + 1

isCorrect = 0

def computeGCD(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x

while True:
    for numb in numbers:
        result = computeGCD(value, numb)

        if result == 1:
            isCorrect = 1

    if isCorrect == 1:
        print(value)
        break

    value += 1






    