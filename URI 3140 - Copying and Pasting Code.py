shouldCopy = False

while True:
    try:
        tag = input()

        if '<body>' in tag:
            shouldCopy = True
            continue
        
        if '</body>' in tag:
            shouldCopy = False

        if shouldCopy == True:
            print(tag)

    except EOFError:
        break