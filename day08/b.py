from math import lcm

def get_steps_to_Z(graph, instruction, start_node):
    curr_node = start_node
    total_steps = 0
    it = 0

    while curr_node[-1] != 'Z':
        total_steps += 1
        direction = instruction[it]
        it = (it + 1) % len(instruction)

        if direction == 'L':
            curr_node = graph[curr_node][0]
        elif direction == 'R':
            curr_node = graph[curr_node][1]

    return total_steps

with open("input.txt", "r") as f:
    lines = f.readlines()

instructions = lines[0].strip()

graph = {}

for line in lines[2:]:
    key = line.split()[0]
    left = line.split()[2][1:-1]
    right = line.split()[3][:-1]

    graph[key] = (left, right)

curr_nodes = set([key for key in graph if key[-1] == 'A'])

total_steps = 1
for node in curr_nodes:
    total_steps = lcm(total_steps, get_steps_to_Z(graph, instructions, node))

print(total_steps)