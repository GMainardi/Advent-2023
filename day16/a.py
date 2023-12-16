import sys
sys.setrecursionlimit(10000)


slash = {
    complex(1, 0): complex(0, -1),
    complex(-1, 0): complex(0, 1),
    complex(0, 1): complex(-1, 0),
    complex(0, -1): complex(1, 0)
}

backslash = {
    complex(1, 0): complex(0, 1),
    complex(-1, 0): complex(0, -1),
    complex(0, 1): complex(1, 0),
    complex(0, -1): complex(-1, 0)
}

upward = complex(-1, 0)
downward = complex(1, 0)
leftward = complex(0, -1)
rightward = complex(0, 1)

def energize(mirror_map: list[str], pos: complex, direction: complex):

    global energized

    w, h = len(mirror_map), len(mirror_map[0])

    if pos.real < 0 or pos.imag < 0 or pos.real >= w or pos.imag >= h:
        return set(energized.keys())
    
    if direction in energized.get(pos, set([])):
        return set(energized.keys())
    
    char = mirror_map[int(pos.real)][int(pos.imag)]

    if pos in energized:
        energized[pos].add(direction)

    else:
        energized[pos] = set([direction])

    if char == '/':
        direction = slash[direction]
    
    elif char == '\\':
        direction = backslash[direction]

    elif char == '|':
        if direction.real == 0:
            up = energize(mirror_map, pos+upward, upward)
            down = energize(mirror_map, pos+downward, downward)
            return up.union(down)
        
    elif char == '-':
        if direction.imag == 0:
            right = energize(mirror_map, pos+rightward, rightward)
            left = energize(mirror_map, pos+leftward, leftward)
            return left.union(right)
        
    return energize(mirror_map, pos+direction, direction)

with open('input.txt') as f:
    mirror_map = [line.strip() for line in f.readlines()]

start = complex(0, 0)
direction = complex(0, 1)
energized = {}
print(len(energize(mirror_map, start, direction)))