while True:
    try:
        N, Q = input().split()

        grades = []

        for grade in range(int(N)):
            grades.append(int(input()))
        
        grades.sort(reverse=True)
        
        for position in range(int(Q)):
            p = int(input())
            grade = grades[p - 1]
            print(grade)

    except EOFError:
        break