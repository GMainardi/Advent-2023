import math

def get_power(game: list) -> bool:

    min_cubes = {'red': 0, 'green': 0, 'blue': 0}

    for round in game:
        for number, color in round:
            if number > min_cubes[color]:
                min_cubes[color] = number
    
    return math.prod(min_cubes.values())

power_sum = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        game_id, game = line.split(':')
        game_id = int(game_id.split(' ')[1])

        rounds = game.split(';')

        game = []
        for round in rounds:
            game.append(
                [(int(number), color) 
                 for number, color in 
                 [show.split() 
                  for show in round.strip().split(',')]])
        
        power_sum += get_power(game)

print(f'Total power: {power_sum}')