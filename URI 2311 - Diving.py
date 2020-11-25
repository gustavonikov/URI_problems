N = int(input())

for player in range(N):
    name = input()
    difficulty = float(input())
    scores = input().split()
    scores = [float(score) for score in scores]

    scores.sort()
    scores.__delitem__(0)
    scores.__delitem__(-1)
    totalScore = sum(scores)
    finalScore = totalScore * difficulty
    
    print('%s %.2f'%(name, finalScore))
