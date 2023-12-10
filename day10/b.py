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
    #print(f'form {form} next {next}')
    for d in next:
        #print(f'direction {d}')
        if (curr[0] + d[0], curr[1] + d[1]) != prev:
            #print((row + d[0], col + d[1]))
            return (row + d[0], col + d[1])

    return None

def monta_poligono(maze):
    arestas = []
    s_aresta = get_start(maze)
    prev = s_aresta
    curr = first_step(maze, prev)

    while maze[curr[0]][curr[1]] != 'S':

        if maze[curr[0]][curr[1]] in ['F', 'J', '7', 'L']:
            arestas.append((s_aresta, curr))
            s_aresta = curr
        prev, curr = curr, next_step(maze, curr, prev)

    arestas.append((s_aresta, curr))
    return arestas

def in_aresta(aresta, ponto):
    p1, p2 = aresta
    
    if ponto[0] >= min(p1[0], p2[0]) and ponto[0] <= max(p1[0], p2[0]) and ponto[1] == p1[1]:
        return True
    
    if ponto[1] >= min(p1[1], p2[1]) and ponto[1] <= max(p1[1], p2[1]) and ponto[0] == p1[0]:
        return True
        
    return False

def is_nest_point(ponto, poligono):
    counts = 0
    for aresta in poligono:

        if in_aresta(aresta, ponto):
            return False

        if aresta[0][0] == aresta[1][0]:
            continue
        
        a_s = min(aresta[0][0], aresta[1][0])
        a_e = max(aresta[0][0], aresta[1][0])


        if ponto[0]+0.1 < a_e and ponto[0]+0.1 > a_s:
            if ponto[1] > aresta[0][1]:
                counts += 1

    return counts % 2 == 1

with open('input.txt', 'r') as f:
    maze = [line.strip() for line in f.readlines()]

poligono = monta_poligono(maze)

nest_points = 0
for row in range(len(maze)):
    for col in range(len(maze[row])):
        if is_nest_point((row, col), poligono):
            maze[row] = maze[row][:col] + 'N' + maze[row][col+1:]
            nest_points += 1

print(nest_points)