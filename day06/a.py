def estimate_race_time(hold_time, distance):
    return distance / hold_time

def get_winning_times(total_time, distance):

    winning_hold_time = 0
    for i in range(1, total_time+1):
        if estimate_race_time(i, distance) < total_time-i:
            winning_hold_time += 1
    return winning_hold_time

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