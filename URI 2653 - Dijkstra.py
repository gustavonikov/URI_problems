jewels = []

while True:
    try:
        jewel = input()
        if not jewels.__contains__(jewel):
            jewels.append(jewel)
        
    except EOFError:
        print(len(jewels))
        break