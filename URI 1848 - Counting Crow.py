responses = []
cawCawCount = 0

while True:
    if cawCawCount == 3:
        break

    crowResponses = input().split()

    if crowResponses == ['caw', 'caw']:
        integerResponses = []
        if len(responses) == 0:
            integerResponse = 0
        else:
            for response in responses:
                firstEye = response[0]
                secondEye = response[1]
                thirdEye = response[2]
                newResponses = [firstEye, secondEye, thirdEye]

                binaryResponse = ''
                for newResponse in newResponses:
                    if newResponse == '-':
                        binaryResponse += '0'
                    else:
                        binaryResponse += '1'
                integerResponse = int(binaryResponse, 2)
                integerResponses.append(integerResponse)

        cawCawCount += 1
        responses = []
        print(sum(integerResponses))
    else:
        for crowResponse in crowResponses:
            responses.append(crowResponse)
