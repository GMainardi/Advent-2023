import sys

sys.setrecursionlimit(10_000)

UP = complex(-1, 0)
DOWN = complex(1, 0)
LEFT = complex(0, -1)
RIGHT = complex(0, 1)

def is_step_valid(step: complex, maze: list[str], visited: set[complex]) -> bool:

    if step in visited:
         return False
    
    if 0 > step.real or step.real >= len(maze):
        return False
    
    if 0 > step.imag or step.imag >= len(maze[0]):
        return False

    if maze[int(step.real)][int(step.imag)] == '#':
        return False
    
    return True

def get_neighbours(pos: complex, maze: list[str], visited: set[complex]) -> list[complex]:

    return [
        pos+neig for neig in [UP, DOWN, LEFT, RIGHT]
            if is_step_valid(pos+neig, maze, visited)
    ]

def go_to_bif(bif: complex, starts: list[complex], maze: list[str]):
    
    paths = []
    for start in starts:
        visited = set([start, bif])
        neighbours = [start]

        while len(neighbours) == 1:

            curr = neighbours[0]

            neighbours = get_neighbours(curr, maze, visited)

            visited.add(curr)

        paths.append(
            {
                'bif': curr,
                'steps': visited
            }
        )
    return paths

def get_all_bifs(maze: list[str]):

    bifs = []

    for y in range(len(maze)):
        for x in range(len(maze[0])):
            
            if maze[y][x] == '#':
                continue

            curr = complex(y, x)

            neighbours = get_neighbours(curr, maze, set([])) 

            if len(neighbours) > 2:
                bifs.append(curr)
    return bifs

def search(node: complex, stop, maze, seen):

    if node == stop:
        return seen

    best = set([])
    for neigh in maze[node]:

        if neigh['bif'] in seen:
            continue
        
        path = search(neigh['bif'], stop, maze, seen.union(neigh['steps']))

        if len(path) > len(best):
            best = path
    
    return best

maze = [line.strip() for line in open('input.txt', 'r').readlines()]
start = complex(0, maze[0].find('.'))
end = complex(len(maze)-1, maze[-1].find('.'))

bifs = get_all_bifs(maze)
bifs.append(start)
bifs.append(end)

new_maze = {}
for bif in bifs:

    new_maze[bif] = go_to_bif(
        bif,
        get_neighbours(bif, maze, set([])),
        maze
    )

import time

s = time.time()
max_path = search(start, end, new_maze, set([start]))
e = time.time()


print(len(max_path)-1)
print(f'Time: {e-s}')
