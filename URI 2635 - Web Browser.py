N = int(input())

searchedWords = []

for searchedWord in range(N):
    word = input()
    searchedWords.append(word)

Q = int(input())

for query in range(Q):
    correspondingWords = []
    lenOfTheWords = []

    queryWord = input()
    queryWordLen = len(queryWord)
    
    for words in searchedWords:
        if queryWord in words[0:queryWordLen]:
            correspondingWords.append(words)
            lenOfTheWords.append(len(words))

    lenOfTheWords.sort(reverse=True)

    if len(correspondingWords) > 0:
        print(len(correspondingWords), lenOfTheWords[0])
    else:
        print(-1)
