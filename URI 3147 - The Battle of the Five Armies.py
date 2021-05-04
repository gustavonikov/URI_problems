humans, elves, dwarves, orcs, wargs, eagles = input().split()
    
goodArmy = int(humans) + int(elves) + int(dwarves) + int(eagles)
badArmy = int(orcs) + int(wargs)

if goodArmy >= badArmy:
    print('Middle-earth is safe.')
else:
    print('Sauron has returned.')