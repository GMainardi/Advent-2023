def is_game_possible(game: list) -> bool:

    max_cubes = {'red': 12, 'green': 13, 'blue': 14}

    for round in game:
        for number, color in round:
            if number > max_cubes[color]:
                return False
    
    return True

possible_sum = 0
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
        
        if is_game_possible(game):
            possible_sum += game_id


print(f'Sum of impossible games: {possible_sum}')
        