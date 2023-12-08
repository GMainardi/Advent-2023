with open("input.txt", "r") as f:
    lines = f.readlines()

instructions = lines[0].strip()

graph = {}

for line in lines[2:]:
    key = line.split()[0]
    left = line.split()[2][1:-1]
    right = line.split()[3][:-1]

    graph[key] = (left, right)

curr_node = 'AAA'
total_steps = 0
it = 0
while curr_node != 'ZZZ':
    total_steps += 1
    direction = instructions[it]
    it = (it + 1) % len(instructions)

    if direction == 'L':
        curr_node = graph[curr_node][0]
    elif direction == 'R':
        curr_node = graph[curr_node][1]

print(total_steps)