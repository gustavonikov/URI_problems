N = int(input())
K = int(input())

scores = []

for competitors in range(N):
    score = int(input())
    scores.append(score)

scores.sort(reverse=True)

classifiedCompetitors = []

for classified in scores[0:K-1]:
    classifiedCompetitors.append(classified)


tiedCompetitors = scores.count(scores[K-1])
classifiedTiedCompetitors = classifiedCompetitors.count(scores[K-1])

matchClassified = tiedCompetitors - classifiedTiedCompetitors

if matchClassified != 0:
    for times in range(matchClassified):
        classifiedCompetitors.append(scores[K-1])

print(len(classifiedCompetitors))