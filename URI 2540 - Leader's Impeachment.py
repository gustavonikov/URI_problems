while True:
    try:
        N = int(input())
        votes = input().split(maxsplit=N)
        votes = [int(vote) for vote in votes]
        votesNeeded = N * (2/3)

        numberOfVotes = votes.count(1)
        if numberOfVotes >= votesNeeded:
            print('impeachment')
        else:
            print('acusacao arquivada')

    except EOFError:
        break