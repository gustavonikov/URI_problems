N = int(input())

sequence = input().split(maxsplit=N)
sequence = [int(number) for number in sequence]

def subtract(index):
    if index < len(sequence) - 1:
        value = sequence[index + 1] - sequence[index]

        return value
    
newSequence = [subtract(index) for index, value in enumerate(sequence)]
stepladders = 1

if newSequence.__contains__(None): newSequence.remove(None)

for index, number in enumerate(newSequence):
    if index != len(newSequence) - 1 and newSequence[index] != newSequence[index + 1]:
        stepladders +=1

print(stepladders)
