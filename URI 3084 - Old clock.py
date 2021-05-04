while True:
    try:
        h, m = input().split()

        hours = int(h) / 30
        minutes = int(m) / 6

        hours, minutes = str(int(hours)), str(int(minutes))

        print(f'{hours.zfill(2)}:{minutes.zfill(2)}')
    
    except EOFError:
        break