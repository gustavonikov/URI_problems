import struct

entries = input().split(maxsplit=3)

intNumb = int(entries[0])
floatNumb = float(entries[1])
floatNumb = struct.unpack('f', struct.pack('f', floatNumb))[0]
character = entries[2]
phrase = ' '.join(entries[3:])

output1 = '{}{:.6f}{}{}'.format(intNumb, floatNumb, character, phrase)
output2 = '{}\t{:.6f}\t{}\t{}'.format(intNumb, floatNumb, character, phrase)
output3 = '{:>10}{:>10.6f}{:>10}{:>10}'.format(intNumb, floatNumb, character, phrase)

print(output1)
print(output2)
print(output3)