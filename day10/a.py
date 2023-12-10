directions = {
    'S': [(0, 1), (0, -1), (1, 0), (-1, 0)],
    '|': [(1, 0), (-1, 0)],
    '-': [(0, 1), (0, -1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)]
}

def get_start(maze):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 'S':
                return (row, col)
            
def first_step(maze, start):
    
    row, col = start

    possible_steps = {
        (row+1, col): ['|', 'L', 'J'],
        (row-1, col): ['|', '7', 'F'],
        (row, col+1): ['-', '7', 'J'],
        (row, col-1): ['-', 'L', 'F']
    }
    for step in possible_steps:
        if maze[step[0]][step[1]] in possible_steps[step]:
            return step
    return None

def next_step(maze, curr, prev):
    row, col = curr
    
    form = maze[row][col]

    next = directions[form]
    for d in next:
        if (curr[0] + d[0], curr[1] + d[1]) != prev:
            return (row + d[0], col + d[1])

    return None

with open('input.txt', 'r') as f:
    maze = [line.strip() for line in f.readlines()]


pipe_l = 1
prev = get_start(maze)
curr = first_step(maze, prev)

while maze[curr[0]][curr[1]] != 'S':
    pipe_l += 1
    prev, curr = curr, next_step(maze, curr, prev)
    

print(pipe_l)
print(pipe_l//2)