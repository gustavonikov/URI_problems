T1, T2, T3, T4 = input().split()
T1, T2, T3, T4 = int(T1), int(T2), int(T3), int(T4)

maxNumberOfDevices = (T1-1) + (T2-1) + (T3-1) + T4
print(maxNumberOfDevices)