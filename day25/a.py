from collections import deque
import random
import sys

sys.setrecursionlimit(100_000)

connections = {}
with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    for line in input:
        key = line.split(':')[0]
        values = line.split(':')[1].split(' ')[1:]
        connections[key] = connections.get(key, []) + values
        for value in values:
            connections[value] = connections.get(value, []) + [key]

def count_connected(graph, start):
    stack = [start]
    visited = set(stack.copy())
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    return len(visited)

def find_path_bfs(graph, start, end):

    if start not in graph or end not in graph:
        return None

    queue = deque([[start]]) 
    visited = set() 

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = path + [neighbor]
                queue.append(new_path)

    return None


total_nodes = len(connections.keys())

connections_counts = {}

for _ in tqdm(range(1_000)):
    start = random.choice(list(connections.keys()))
    end = random.choice(list(connections.keys()))

    while start == end:
        end = random.choice(list(connections.keys()))


    path = find_path_bfs(connections, start, end)

    for n1, n2 in zip(path, path[1:]):
        if (n1, n2) in connections_counts:
            connections_counts[(n1, n2)] += 1
        elif (n2, n1) in connections_counts:
            connections_counts[(n2, n1)] += 1
        else:
            connections_counts[(n1, n2)] = 1

top_connections = sorted(connections_counts.items(), key=lambda x: x[1], reverse=True)[:3]

for (c1, c2), _ in top_connections:
    connections[c1].remove(c2)
    connections[c2].remove(c1)

group_nodes = count_connected(connections, list(connections.keys())[0])

print(group_nodes * (total_nodes - group_nodes))