
def get_col(pattern, col):
    if col < 0:
        raise IndexError
    
    return [row[col] for row in pattern]

def get_row(pattern, row):
    if row < 0:
        raise IndexError
    
    return pattern[row]

def count_diff(line1, line2):
    count = 0

    for idx in range(len(line1)):
        if line1[idx] != line2[idx]:
            count += 1

    return count

def count_mirror(pattern, start, get_line, total_mistakes):
    count = 2

    try:

        while total_mistakes < 2:
            total_mistakes += count_diff(
                get_line(pattern, start + count-1), 
                get_line(pattern, start - count)
            )
            count += 1

    except IndexError:
        return total_mistakes == 1
    
    return False

def find_mirror(pattern, length, get_line):

    prev = get_line(pattern, 0)


    for idx in range(1, length):
        col = get_line(pattern, idx)

        diff = count_diff(prev, col)
        
        if diff < 2:

            reflex = count_mirror(pattern, idx, get_line, diff)

            if reflex:
                return idx

        prev = col

    return -1

with open('input.txt') as f:
    patterns = [ pattern.split('\n') for pattern in f.read().split('\n\n')]

total = 0


for pattern in patterns:
    
    horizontal= find_mirror(pattern, len(pattern), get_row)

    if horizontal != -1:
        total += horizontal * 100
    else:
        vertical= find_mirror(pattern, len(pattern[0]), get_col)
        total += vertical

print(total)