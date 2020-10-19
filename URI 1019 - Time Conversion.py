N = int(input())

hours = int(N/3600)
minutes = int((N - (hours * 3600))/60)
seconds = N - (hours * 3600 + minutes * 60)

print('%i:%i:%i'%(hours, minutes, seconds))