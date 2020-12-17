Ca, Ba, Pa = input().split()
Cr, Br, Pr = input().split()

passengersWithoutMeal = 0

if int(Cr) > int(Ca):
    passengersWithoutMeal += (int(Cr) - int(Ca))
if int(Br) > int(Ba):
    passengersWithoutMeal += (int(Br) - int(Ba))
if int(Pr) > int(Pa):
    passengersWithoutMeal += (int(Pr) - int(Pa))

print(passengersWithoutMeal)