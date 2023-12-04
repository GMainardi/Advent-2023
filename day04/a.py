def parse_card(line: str) -> tuple[set, set]:
    numbers = line.split(':')[1]
    
    my_numbers, winner_numbers = numbers.split('|')  
    my_numbers = set(my_numbers.split())
    winner_numbers = set(winner_numbers.split())

    return my_numbers, winner_numbers

def get_card_value(my_numbers: set, winner_numbers: set) -> int:
    winning_set = my_numbers.intersection(winner_numbers)
    if len(winning_set) == 0:
        return 0

    return 2**(len(winning_set)-1)


with open('input.txt') as f:
    total_points = 0
    for line in f.readlines():
        my_numbers, winner_numbers = parse_card(line)
        card_value = get_card_value(my_numbers, winner_numbers)
        total_points += card_value

print(total_points)
    