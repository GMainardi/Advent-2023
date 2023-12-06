from math import sqrt, ceil, floor

def delta(t, d):
    return t**2 - 4*d

def round_start(start):
    if int(start) == start:
        return start + 1
    return ceil(start)

def round_end(end):
    if int(end) == end:
        print(end)
        return end - 1
    
    return floor(end)

def get_winning_times(total_time, distance):

    start = total_time - sqrt(delta(total_time, distance))

    start = round_start(start / 2)

    end = total_time + sqrt(delta(total_time, distance))
    end = round_end(end / 2)

    return end - start + 1

with open('input.txt', 'r') as f:
    lines = f.readlines()

time = int(lines[0].split(':')[1].replace(' ', ''))
distance = int(lines[1].split(':')[1].replace(' ', ''))

print(get_winning_times(time, distance))