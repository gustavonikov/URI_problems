while True:
    try:
        N, D = input().split()
        infos = []    

        for dates in range(int(D)):
            info = input().split()
            infos.append(info)
        
        date = ''

        for info in infos:
            infoWithoutTheDate = info[1:]
            infoWithoutTheDate = [int(info) for info in infoWithoutTheDate]
            if sum(infoWithoutTheDate) == int(N):
                date += info[0]
                break
        
        if date == '':
            print('Pizza antes de FdI')
        else:
            print(date)

    except EOFError:
        break