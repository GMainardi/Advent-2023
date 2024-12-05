import random

input = {}

with open('day25/example.txt') as f:
    lines = f.readlines()

    for line in lines:

        key = line.strip().split(':')[0]
        values = line.strip().split(':')[1].split(' ')[1:]

        input[key] = input.get(key, []) + values
        for value in values:
            input[value] = input.get(value, []) + [key]

def remove_connections(input, c1, c2, c3):
    input[c1[0]].remove(c1[1])
    input[c1[1]].remove(c1[0])
    input[c2[0]].remove(c2[1])
    input[c2[1]].remove(c2[0])
    input[c3[0]].remove(c3[1])
    input[c3[1]].remove(c3[0])

def count_connections(input, start):
    queue = [start]
    visited = set(queue.copy())

    while queue:
        current = queue.pop(0)
        
        if current not in input.keys():
            continue

        for connection in input[current]:
            if connection not in visited:
                visited.add(connection)
                queue.append(connection)

    return visited

def find_path(input, curr, end, visited):
    visited.add(curr)

    if curr == end:
        return [curr]

    for connection in input[curr]:
        if connection not in visited:
            path = find_path(input, connection, end, visited)
            if path:
                return [curr] + path

    return []


total_count = count_connections(input, list(input.keys())[0])

connections = {}
for key in input.keys():
    for value in input[key]:
        if (value, key) not in connections.keys():
            connections[(key, value)] = 0

for i in range(0, 100_000):

    start = random.choice(list(input.keys()))
    end = random.choice(list(input.keys()))

    while start == end:
        end = random.choice(list(input.keys()))

    path = find_path(input, start, end, set())

    for c1, c2 in zip(path, path[1:]):
        if (c1, c2) in connections.keys():
            connections[(c1, c2)] += 1
        else:
            connections[(c2, c1)] += 1

c1, c2, c3 = sorted(connections, key=connections.get, reverse=True)[:3]

print(c1, c2, c3)

remove_connections(input, c1, c2, c3)

new_count = count_connections(input, list(input.keys())[0])

print((len(total_count) - len(new_count)) * len(new_count))