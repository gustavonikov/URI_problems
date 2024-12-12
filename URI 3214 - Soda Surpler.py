E, F, C = input().split()
E, F, C = int(E), int(F), int(C)

sodas_traded = (E + F) // C 
sodas_left = (E + F) % C
sodas_empty =  sodas_traded + sodas_left
sodas_drank = sodas_traded

while True:
  sodas_traded = sodas_empty // C
  sodas_left = sodas_empty % C
  sodas_empty = sodas_traded + sodas_left

  sodas_drank += sodas_traded

  if sodas_empty < C:
    break

print(int(sodas_drank))
