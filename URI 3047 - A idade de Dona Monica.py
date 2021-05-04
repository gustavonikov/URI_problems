M = int(input())
A = int(input())
B = int(input())

otherSonAge = M - A - B

sonsAge = [A, B, otherSonAge]
ageOfTheOldestSon = max(sonsAge)

print(ageOfTheOldestSon)