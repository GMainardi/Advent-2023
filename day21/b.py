def tile_distance(start, walls, lenght):
    min_distances = {start: 0}
    distance = 0
    queue = [start]
    while queue:
        new_queue = []
        for place in queue:
            for direction in [1, -1, 1j, -1j]:
                new_place = place + direction
                if new_place.real < 0 or new_place.real >= lenght or new_place.imag < 0 or new_place.imag >= lenght:
                    continue
                if new_place not in walls and new_place not in min_distances:
                    min_distances[new_place] = distance + 1
                    new_queue.append(new_place)
        queue = new_queue
        distance += 1

    return min_distances


with open('input.txt') as f:
    lines = f.readlines()
    walls = [complex(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == '#']
    start = [complex(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == 'S'][0]
    lenght = len(lines)

tile_distances = tile_distance(start, walls, lenght)

odds = sum(i%2 for i in tile_distances.values())
evens = sum(1-(i%2) for i in tile_distances.values())

c_odds = sum(i%2 for i in tile_distances.values() if i > 65)
c_evens = sum(1-(i%2) for i in tile_distances.values() if i > 65)


n = 202300
full_odds = (n+1)**2 * odds
full_evens = n**2 * evens
odd_corners = (n+1) * c_odds
even_corners = n * c_evens

print(full_odds + full_evens - odd_corners + even_corners)