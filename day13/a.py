
def get_col(pattern, col):
    if col < 0:
        raise IndexError
    
    return [row[col] for row in pattern]

def get_row(pattern, row):
    if row < 0:
        raise IndexError
    
    return pattern[row]

def count_mirror(pattern, start, get_line):
    count = 1

    try:
        while get_line(pattern, start + count-1) == get_line(pattern, start - count):
            count += 1
    except IndexError:
        return count

    return -1

def find_mirror(pattern, length, get_line):

    prev = get_line(pattern, 0)

    for idx in range(1, length):
        col = get_line(pattern, idx)

        if prev == col:
            reflexion_size = count_mirror(pattern, idx, get_line)

            if reflexion_size != -1:
                return (reflexion_size, idx)

        prev = col

    return (-1, -1)

with open('input.txt') as f:
    patterns = [ pattern.split('\n') for pattern in f.read().split('\n\n')]

total = 0


for pattern in patterns:
    
    horizontal_pattern = find_mirror(pattern, len(pattern), get_row)

    if horizontal_pattern[1] != -1:
        total += horizontal_pattern[1] * 100
    else:
        vertical_pattern = find_mirror(pattern, len(pattern[0]), get_col)
        total += vertical_pattern[1]

print(total)