def parse_card(line: str) -> tuple[set, set]:
    numbers = line.split(':')[1]
    
    my_numbers, winner_numbers = numbers.split('|')  
    my_numbers = set(my_numbers.split())
    winner_numbers = set(winner_numbers.split())

    return my_numbers, winner_numbers

def count_winning_cards(my_numbers: set, winner_numbers: set) -> int:
    winning_set = my_numbers.intersection(winner_numbers)
    return len(winning_set)


with open('input.txt') as f:
    lines = f.readlines()
    my_cards = {i: 1 for i in range(len(lines))}

    for idx, line in enumerate(lines):
        my_numbers, winner_numbers = parse_card(line)
        winning_cards = count_winning_cards(my_numbers, winner_numbers)
        for i in range(idx+1, idx+winning_cards+1):
            my_cards[i] += my_cards[idx]


print(sum([v for k, v in my_cards.items()]))
    