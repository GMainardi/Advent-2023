
def gravity_up(moving_rocks, static_rocks, col):
    
    floors = [x[0] for x in static_rocks if x[1] == col] + [-1]
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
    len_x, len_y = x+1, y+1

#show_rocks(moving_rocks, static_rocks)
#print()

new_rocks = set([])
for col in range(len_y):
    new_rocks |= gravity_up(moving_rocks, static_rocks, col)

#show_rocks(new_rocks, static_rocks)


print(sum(len_x - rock[0] for rock in new_rocks))
