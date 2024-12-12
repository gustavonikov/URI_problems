floors, start, goal, floors_per_press_up, floors_per_press_down = map(int, input().split())
floors_diff = goal - start

a = floors_per_press_up 
b = -floors_per_press_down
x = 0.0
y = 0.0

if floors_per_press_up == floors_per_press_down and floors_per_press_up != 0 and (floors_diff % floors_per_press_up != 0) \
  or (floors_diff % 2 != 0 and floors_per_press_up % 2 == 0 and floors_per_press_down % 2 == 0) \
  or (floors_diff != 0 and floors_diff % 2 == 0 and floors_per_press_up % 2 != 0 and floors_per_press_down % 2 != 0):

  print('use the stairs')
else:
  if (floors_diff > 0):
    if floors_per_press_up == 0 or floors_per_press_up > floors:
      print('use the stairs')
    else:
      while True:
        x = (abs(floors_diff) - b * y) / a

        if x.is_integer():
          break

        y += 1
       
      print(int(abs(x + y)))
  elif (floors_diff < 0):
    if floors_per_press_down == 0 or floors_per_press_down > floors:
      print('use the stairs')
    else:
      while True:
        y = (floors_diff - a * x) / b

        if y.is_integer():
          break

        x += 1

      print(int(abs(x + y)))
  else:
    print(0)
    