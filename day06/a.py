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

def line_to_int_list(line):
    return list(map(int, line.strip().split()))

with open('input.txt', 'r') as f:
    lines = f.readlines()

times = line_to_int_list(lines[0].split(':')[1])
distances = line_to_int_list(lines[1].split(':')[1])

races = list(zip(times, distances))

ans = 1
for race in races:
    ans *= get_winning_times(*race)


print(ans)