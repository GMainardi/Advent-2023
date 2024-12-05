import numpy as np

class Hailstone:

    def __init__(self, line):
        line = line.strip().replace(' ', '').split('@')

        possitions = list(map(int, line[0].split(',')))
        directions = list(map(int, line[1].split(',')))

        self.px = possitions[0]
        self.py = possitions[1]
        self.pz = possitions[2]

        self.vx = directions[0]
        self.vy = directions[1]
        self.vz = directions[2]

    def get_crossing_path(self, other: "Hailstone"):


        a1 = self.vx
        b1 = -other.vx
        c1 = other.px - self.px

        a2 = self.vy
        b2 = -other.vy
        c2 = other.py - self.py

        det = a1 * b2 - a2 * b1


        if det == 0:
            return None
        
        t = (c1 * b2 - c2 * b1) / det
        s = (a1 * c2 - a2 * c1) / det

        if t < 0 or s < 0:
            return None
        
        x = self.px + self.vx * t
        y = self.py + self.vy * t

        return x, y

    def __repr__(self):
        return f'pos=<x={self.px}, y={self.py}, z={self.pz}>, vel=<x={self.vx}, y={self.vy}, z={self.vz}>'

input = [Hailstone(line.strip()) for line in open('input.txt', 'r')]

range = (
    200_000_000_000_000, 
    400_000_000_000_000)

crossing_count = 0
for idx, h1 in enumerate(input):
    for h2 in input[idx+1:]:
        crossing_path = h1.get_crossing_path(h2)
        if crossing_path:
            x, y = crossing_path

            if not (range[0] <= x <= range[1] and range[0] <= y <= range[1]):
                continue
        
            crossing_count += 1
            # print(f'A: {h1}')
            # print(f'B: {h2}')
            # print(f'Crossing path at: {x}, {y}')

print(f'Crossing count: {crossing_count}')