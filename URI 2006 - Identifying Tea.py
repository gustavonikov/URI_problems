T = input()

contestantsAnswers = input().split()
countCorrectAnswer = 0

for answers in contestantsAnswers:
    if answers == T:
        countCorrectAnswer += 1

print(countCorrectAnswer)
