A, B, C, D = input().split()

array = [int(A), int(B), int(C), int(D)]
responses = []

for index, lengths in enumerate(array):
    array_copy = array.copy()
    array_copy.__delitem__(index)

    array_copy.sort(reverse=True)
    
    if array_copy[0] >= (array_copy[1] + array_copy[2]):
        responses.append('N')
    else:
        responses.append('S')

if responses.__contains__('S'):
    print('S')
else:
    print('N')
