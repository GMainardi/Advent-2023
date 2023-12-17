from collections import defaultdict
from heapq import heappush, heappop

UP = complex(-1, 0)
DOWN = complex(1, 0)
LEFT = complex(0, -1)
RIGHT = complex(0, 1)

DIRECTIONS = {
    UP: [LEFT, RIGHT],
    DOWN: [LEFT, RIGHT],
    LEFT: [UP, DOWN],
    RIGHT: [UP, DOWN]
}

with open('input.txt') as f: 
    MAP = [[int(x) for x in line.strip()] for line in f.readlines()]

DEST = complex(len(MAP)-1, len(MAP[0])-1)
START = complex(0, 0)

def in_bounds(point: complex):
    return 0 <= point.real < len(MAP) and 0 <= point.imag < len(MAP[0])    


def dijkstra():

    dists = defaultdict(lambda: float('inf'))
    
    heap = [
        (0, id(START), (START, RIGHT)),
        (0, id(START), (START, DOWN))
    ]

    while heap:
        cost, _, (curr, dir) = heappop(heap)

        if curr == DEST:
            return cost
        
        if cost > dists[curr, dir]:
            continue
        
        for direction in DIRECTIONS[dir]:
            ncost = cost

            for streak in range(1, 11):

                next = curr + direction * streak

                if not in_bounds(next):
                    continue

                ncost += MAP[int(next.real)][int(next.imag)]

                if streak < 4:
                    continue

                item = (next, direction)
                if ncost < dists[item]:
                    dists[item] = ncost
                    heappush(heap, (ncost, id(next), item))
    return -1
print(dijkstra())