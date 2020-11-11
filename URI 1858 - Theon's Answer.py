N = int(input())

personNumbers = input().split(maxsplit=N)

personNumbers_copy = personNumbers.copy()

personNumbers_copy.sort()
personThatWillResultInFewestHits = personNumbers_copy[0]

indexOfThePerson = personNumbers.index(personThatWillResultInFewestHits) + 1
print(indexOfThePerson)
