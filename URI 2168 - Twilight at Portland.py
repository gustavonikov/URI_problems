N = int(input())

blocks = []

for lines in range(N + 1):
    cameraStatus = input().split(maxsplit=(N + 1))
    cameraStatus = [int(status) for status in cameraStatus]
    blocks.append(cameraStatus)

for lineIndex, line in enumerate(blocks[:-1]):
    result = ''
    for elementIndex, element in enumerate(line[:-1]):
        blockArray = [element, line[elementIndex + 1], blocks[lineIndex + 1][elementIndex], blocks[lineIndex + 1][elementIndex + 1]]
        if sum(blockArray) >= 2:
            result += 'S'
        else:
            result += 'U'
    print(result)