DIRECTIONS = [
    complex(1, 0),
    complex(0, -1),
    complex(-1, 0),
    complex(0, 1) 
]

def get_polygon_area(polygon):
    area_plus = sum(polygon[i].real * polygon[i + 1].imag for i in range(len(polygon) - 1))
    area_minus = sum(polygon[i].imag * polygon[i + 1].real for i in range(len(polygon) - 1))

    return abs(area_plus - area_minus) / 2

with open('input.txt') as f:
    dig_plan = [line.strip().split(' ') for line in f.readlines()]

polygon = [complex(0, 0)]

map_l = ['R', 'D', 'L', 'U']
lenght = 0
for dig in dig_plan:
    direction = DIRECTIONS[int(dig[2][-2])]
    distance = int(dig[2][2:-2], 16)
    lenght += distance
    polygon.append(polygon[-1] + direction * distance)

area = get_polygon_area(polygon)

print(int(area + lenght / 2 + 1))