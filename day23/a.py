import sys

sys.setrecursionlimit(10_000)

maze = [line for line in open('example.txt', 'r').readlines()]

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
    
    if maze[int(pos.real)][int(pos.imag)] == '>':
        return [pos+RIGHT] if is_step_valid(pos+RIGHT, maze, visited) else []
    
    if maze[int(pos.real)][int(pos.imag)] == '<':
        return [pos+LEFT] if is_step_valid(pos+LEFT, maze, visited) else []
    
    if maze[int(pos.real)][int(pos.imag)] == '^':
        return [pos+UP] if is_step_valid(pos+UP, maze, visited) else []
    
    if maze[int(pos.real)][int(pos.imag)] == 'v':
        return [pos+DOWN] if is_step_valid(pos+DOWN, maze, visited) else []

    return [
        pos+neig for neig in [UP, DOWN, LEFT, RIGHT]
            if is_step_valid(pos+neig, maze, visited)
    ]

def find_max_path(start: complex, end: complex, maze: list[str], visited: set[complex], steps: int):
    
    if not(len(get_neighbours(start, maze, visited))):
        return -1
    
    farest = 0
    for neigh in get_neighbours(start, maze, visited):

        if neigh == end:
            return steps + 1
        
        farest = max(
            farest, 
            find_max_path(neigh, end, maze, visited.union(set([neigh])), steps+1)
            )
        
    return farest

start = complex(0, maze[0].find('.'))
end = complex(len(maze)-1, maze[-1].find('.'))
visited = set([start])

print(find_max_path(
    start, end,
    maze, visited,
    0
))
        