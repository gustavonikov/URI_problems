while True:
    try:
        decipherCode = {}
        C, N = input().split()
        N = int(N)
        cipher = input().lower()
        decipheredCipher = input().lower()

        for index, letter in enumerate(cipher):
            decipherCode[letter] = decipheredCipher[index]
        
        for phrases in range(N):
            phraseToDecipher = input().split(sep='ç')

            decipheredPhrase = []
            
            for sentenceIndex, sentence in enumerate(phraseToDecipher):
                newSentence = ''
                
                for letterIndex, letter in enumerate(sentence, 1):
                    letterLowerCase = letter.lower()
                    letterIsLower = True

                    if letterLowerCase != letter:
                        letterIsLower = False

                    for code, decode in decipherCode.items():
                        if letterLowerCase == code:
                            if letterIsLower == True:
                                newSentence += decode
                            else:
                                newSentence += decode.capitalize()      
                        elif letterLowerCase == decode:
                            if letterIsLower == True:
                                newSentence += code
                            else:
                                newSentence += code.capitalize()
                            
                    if len(newSentence) != letterIndex:
                        newSentence += letter
                
                decipheredPhrase.append(newSentence)
            print(*decipheredPhrase)
        print()

    except EOFError:
        break
