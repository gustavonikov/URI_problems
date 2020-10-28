S = 0
count = 0

for sequenceNumber in range(1, 41, 2):
    S += (sequenceNumber/2**count)
    count += 1

print('%.2f'%S)