while True:
    try:
        N, I = input().split()

        csVideos = 0

        for videos in range(int(N)):
            i, j = input().split()

            if i == I and j == '0':
                csVideos += 1
        
        print(csVideos)

    except EOFError:
        break
