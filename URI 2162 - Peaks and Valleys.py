N = int(input())

measures = input().split()

measures = [int(measure) for measure in measures]

isTheSamePatternAsNlogony = True

if measures[0] == measures[1]:
    isTheSamePatternAsNlogony = False
elif measures[0] > measures[1]:
    for index, measure in enumerate(measures[1:], 1):
        if index % 2 != 0 and measure >= measures[index - 1]:
            isTheSamePatternAsNlogony = False
            break
        
        if N % 2 != 0 and measures[-1] <= measures[-2]:
            isTheSamePatternAsNlogony = False
            break
elif measures[0] < measures[1]:
    for index, measure in enumerate(measures[1:], 1):
        if index % 2 != 0 and measure <= measures[index - 1]:
            isTheSamePatternAsNlogony = False
            break

        if N % 2 != 0 and measures[-1] >= measures[-2]:
            isTheSamePatternAsNlogony = False
            break

if isTheSamePatternAsNlogony == True:
    print(1)
else:
    print(0)