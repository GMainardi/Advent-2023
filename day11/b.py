def get_empty_rows(space):
    empty_rows = []
    for idx, row in enumerate(space):
        if all([x == '.' for x in row]):
            empty_rows.append(idx)
    return empty_rows

def get_empty_cols(space):
    empty_cols = []
    for idx in range(len(space[0])):
        if all([x[idx] == '.' for x in space]):
            empty_cols.append(idx)
    return empty_cols

def get_true_galax_pos(pos, empty_cols, empty_rows):
    x, y = pos
    double_cols = [col_idx for col_idx in empty_cols if col_idx < x]
    double_rows = [row_idx for row_idx in empty_rows if row_idx < y]

    return (x+(len(double_cols)*999999), y+(len(double_rows)*999999))

def manhattan_distance(p1, p2):
    x = abs(p1[0] - p2[0])
    y = abs(p1[1] - p2[1])
    return x + y

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

empty_rows = get_empty_rows(lines)
empty_cols = get_empty_cols(lines)

galaxies = []
for y, row in enumerate(lines):
    for x, char in enumerate(row):
        if char == '#':
            galaxies.append(
                get_true_galax_pos(
                    (x, y), 
                    empty_cols, 
                    empty_rows
                )
            )

total_distances = 0
for idx, p1 in enumerate(galaxies):
    for p2 in galaxies[idx+1:]:
        total_distances += manhattan_distance(p1, p2)

print(total_distances)