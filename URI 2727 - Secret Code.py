while True:
    try:
        N = int(input())

        for lines in range(N):
            line = input().split()

            indice = 0
            count = 0
            code = line[0]
            
            for codes in line:
                count += len(codes)

            if len(code) == 1:
                indice = (len(line) - 1) * 2 + count
            elif len(code) == 2:
                indice = (len(line) - 1) * 1 + count
            elif len(code) == 3:
                indice = count

            letter = chr(ord('`') + indice)
            print(letter)

    except EOFError:
        break
