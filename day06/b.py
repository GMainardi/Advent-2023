def estimate_race_time(hold_time, distance):
    return distance / hold_time

def get_winning_times(total_time, distance):

    winning_hold_time = 0

    for i in range(1, total_time+1):
        if estimate_race_time(i, distance) < total_time-i:
            winning_hold_time += 1
    return winning_hold_time

with open('input.txt', 'r') as f:
    lines = f.readlines()

time = int(lines[0].split(':')[1].replace(' ', ''))
distance = int(lines[1].split(':')[1].replace(' ', ''))

print(get_winning_times(time, distance))