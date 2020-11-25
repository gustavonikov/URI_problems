N = int(input())

measures = input().split()

measures = [int(measure) for measure in measures]

speedFallHappens = False
firstSpeedFall = 0

for index, measure in enumerate(measures[1:], 1):
    if measure < measures[index - 1]:
        speedFallHappens = True
        firstSpeedFall = index + 1
        break

print(firstSpeedFall)