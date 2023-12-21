with open('input.txt') as f:
    lines = f.readlines()
    walls = [complex(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == '#']
    start = [complex(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == 'S'][0]
    lenght = len(lines)

def step(current, walls, lenght):
    new_places = set([])
    for place in current:
        for direction in [1, -1, 1j, -1j]:
            new_place = place + direction
            if new_place.real < 0 or new_place.real >= lenght or new_place.imag < 0 or new_place.imag >= lenght:
                continue
            if new_place not in walls:
                new_places.add(new_place)
    return new_places


current = set([start])
for i in range(64):
    current = step(current, walls, lenght)
    print(len(current))

print(len(current))

