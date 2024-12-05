import numpy as np
from sympy import Symbol
from sympy import solve_poly_system

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


x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
vx = Symbol('vx')
vy = Symbol('vy')
vz = Symbol('vz')

equations = []
t_syms = []

for idx, shard in enumerate(input[:3]):
    t = Symbol(f't{idx}')

    eqx = x + vx * t - shard.px - shard.vx * t
    eqy = y + vy * t - shard.py - shard.vy * t
    eqz = z + vz * t - shard.pz - shard.vz * t

    equations.append(eqx)
    equations.append(eqy)
    equations.append(eqz)
    t_syms.append(t)

result = solve_poly_system(equations, *([x,y,z,vx,vy,vz]+t_syms))
print(result)
print(sum(result[0][:3]))