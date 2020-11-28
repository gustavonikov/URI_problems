while True:
    try:
        N, M = input().split()
        
        array = []

        for row in range(int(N)):
            cells = input().split()
            cells = [9 if cell == '1' else int(cell) for cell in cells]
            array.append(cells)

        for rowIndex, row in enumerate(array):
            for index, element in enumerate(row):
                if element == 0 and rowIndex != (int(N) - 1) and array[rowIndex + 1][index] == 9:
                    row[index] += 1
                if element == 0 and rowIndex != 0 and array[rowIndex - 1][index] == 9:
                    row[index] += 1
                if element == 0 and index != (int(M) - 1) and row[index + 1] == 9:
                    row[index] += 1
                if element == 0 and index != 0 and row[index - 1] == 9:
                    row[index] += 1
        
        for rows in array:
            print(*rows, sep='')

    except EOFError:
        break