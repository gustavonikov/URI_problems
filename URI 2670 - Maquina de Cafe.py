A1 = int(input())
A2 = int(input())
A3 = int(input())

employeesPerFloor = [A1, A2, A3]

firstFloorChoice = (A3 * 4 + A2 * 2)
secondFloorChoice = (A3 * 2 + A1 * 2)
thirdFloorChoice = (A1 * 4 + A2 * 2)
chosenFloor = 1

if thirdFloorChoice < secondFloorChoice and thirdFloorChoice < firstFloorChoice:
    chosenFloor = 2
elif firstFloorChoice < secondFloorChoice and firstFloorChoice < thirdFloorChoice:
    chosenFloor = 0
elif secondFloorChoice < thirdFloorChoice and secondFloorChoice < firstFloorChoice:
    chosenFloor = 1

result = 0

for floorIndex, employees in enumerate(employeesPerFloor):
    totalMinutes = (abs(chosenFloor - floorIndex) * 2) * employees
    result += totalMinutes

print(result)
