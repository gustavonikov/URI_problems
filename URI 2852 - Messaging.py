K = input()
N = int(input())

for test in range(N):
    words = input().split()

    phrase = ''
    count = 0

    for index, word in enumerate(words):
        if word[0] != 'a' and word[0] != 'e' and word[0] != 'i' and word[0] != 'o' and word[0] != 'u':
            newWord = ''
            
            for letter in word:
                if count == len(K):
                    count = 0

                convertedLetterToUnicode = (ord(letter) - 96) + (ord(K[count]) - 96) - 1

                if convertedLetterToUnicode > 26:
                    convertedLetterToUnicode = convertedLetterToUnicode - 26

                convertedUnicodeToLetter = chr(ord('`')+convertedLetterToUnicode)
                newWord += convertedUnicodeToLetter
                count += 1
            
            if index == 0:
                phrase += newWord
            else:
                phrase += ' ' + newWord
        else:
            if index == 0:
                phrase += word
            else:
                phrase += ' ' + word
    
    print(phrase)