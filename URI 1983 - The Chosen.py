n = int(input())
listOfStudents = []

for students in range(n):
    infos = input().split()
    infos[1] = float(infos[1])
    listOfStudents.append(infos)

dictionaryOfStudents = dict(listOfStudents)

grades = []

for students in listOfStudents:
    if students[1] >= 8:
        grades.append(students[1])

grades.sort(reverse=True)

if len(grades) > 0:
    for RG, grade in dictionaryOfStudents.items():
        if grade == grades[0]:
            print(RG)
else:
    print('Minimum note not reached')