
def gravity_left(moving_rocks, static_rocks, row):
    
    floors = [-1] + [x[1] for x in static_rocks if x[0] == row]
    floors.sort()
    
    rocks = [x[1] for x in moving_rocks if x[0] == row]
    rocks.sort()

    floor_idx = 0
    new_rocks = []

    for rock in rocks:

        while floor_idx+1 < len(floors) and rock > floors[floor_idx+1]:
            floor_idx += 1
        
        floors[floor_idx] += 1
        new_rocks.append((row, floors[floor_idx]))

    return set(new_rocks)

def gravity_right(moving_rocks, static_rocks, row):
        
    global length
    floors = [x[1] for x in static_rocks if x[0] == row] + [length]
    floors.sort(reverse=True)
    
    rocks = [x[1] for x in moving_rocks if x[0] == row]
    rocks.sort(reverse=True)


    floor_idx = 0
    new_rocks = []

    for rock in rocks:
        
        while floor_idx+1 < len(floors) and rock < floors[floor_idx+1]:
            floor_idx += 1
    
        floors[floor_idx] -= 1
        new_rocks.append((row, floors[floor_idx]))

    return set(new_rocks)

def gravity_down(moving_rocks, static_rocks, col):

    global length

    floors = [x[0] for x in static_rocks if x[1] == col] + [length]
    floors.sort(reverse=True)
    
    rocks = [x[0] for x in moving_rocks if x[1] == col]
    rocks.sort(reverse=True)

    floor_idx = 0
    new_rocks = []

    for rock in rocks:

        while floor_idx+1 < len(floors) and rock < floors[floor_idx+1]:
            floor_idx += 1
    
        floors[floor_idx] -= 1
        new_rocks.append((floors[floor_idx], col))

    return set(new_rocks)

def gravity_up(moving_rocks, static_rocks, col):
    
    floors = [-1] + [x[0] for x in static_rocks if x[1] == col]
    floors.sort()
    
    rocks = [x[0] for x in moving_rocks if x[1] == col]
    rocks.sort()

    floor_idx = 0
    new_rocks = []

    for rock in rocks:

        while floor_idx+1 < len(floors) and rock > floors[floor_idx+1]:
            floor_idx += 1
        
        floors[floor_idx] += 1
        new_rocks.append((floors[floor_idx], col))

    return set(new_rocks)

def apply_gravity(moving_rocks, static_rocks, gravity_func):

    global length
    new_rocks = set([])
    for idx in range(length):
        new_rocks |= gravity_func(moving_rocks, static_rocks, idx)
    return new_rocks

def cicle(moving_rocks, static_rocks):
    turning_cicle = [
        gravity_up, 
        gravity_left, 
        gravity_down, 
        gravity_right
    ]

    for i in range(4):
        
        new_rocks = apply_gravity(moving_rocks, static_rocks, turning_cicle[i])
        moving_rocks = new_rocks

    return moving_rocks

def show_rocks(moving_rocks, static_rocks):
    for x in range(10):
        for y in range(10):
            if (x, y) in moving_rocks:
                print('O', end='')
            elif (x, y) in static_rocks:
                print('#', end='')
            else:
                print('.', end='')
        print('')

static_rocks = set([])
moving_rocks = set([])

with open('input.txt') as f:

    
    for x, row in enumerate(f.readlines()):
        for y, col in enumerate(row.strip()):
            if col == 'O':
                moving_rocks.add((x, y))
            elif col == '#':
                static_rocks.add((x, y))
    length = x+1


cache = {}
turns = 1_000_000_000
turn = 0

while turn < turns:

    if tuple(moving_rocks) in cache:
        period = turn - cache[tuple(moving_rocks)]

        if turn % period == turns % period:
            break
    else:
        cache[tuple(moving_rocks)] = turn

    new_rocks = cicle(moving_rocks, static_rocks)
    moving_rocks = new_rocks
    turn += 1


print(sum(length - rock[0] for rock in new_rocks))
