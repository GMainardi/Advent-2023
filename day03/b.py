'''
input format:
467..114..
...*......
..35..633.
......#...
617*......
.....+$58.
..592.....
......755.
...$.*....
.664.598..
'''

SYMBOLS = ['*', '#', '$', '+', '@', '&', '/', '=', '-', '%']

def get_number_end_pos(line, start_pos):

    curr_pos = start_pos[0]

    while curr_pos < len(line):
        
        if line[curr_pos] in SYMBOLS + ['.']: 
            return (starter_pos[0], 
                    curr_pos - 1, 
                    start_pos[1],
                    line[start_pos[0]:curr_pos])
        
        curr_pos += 1

    return (start_pos[0], 
            curr_pos, 
            start_pos[1],
            line[start_pos[0]:curr_pos])   


def is_adjacent(number, symbol):

    start_x, end_x, y, _ = number
    symbol_x, symbol_y = symbol

    if symbol_y+1 == y or symbol_y-1 == y:
        return symbol_x <= end_x+1 and symbol_x >= start_x-1

    return (symbol_x == start_x-1 or symbol_x == end_x+1) and symbol_y == y

def get_gear_ration(symbol, numbers_pos):
    adjs = []
    for number in numbers_pos:
        if is_adjacent(number, symbol):
            adjs.append(number)
    
    return adjs

number_pos = set([])
symbol_pos = set([])
with open('input.txt', 'r') as f:
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line.strip()):
            
            if c == '.': continue
            elif c == '*': 
                symbol_pos.add((x, y))
            elif c not in SYMBOLS:
                if x - 1 >= 0 and line[x-1] not in SYMBOLS + ['.']: continue
                starter_pos = (x, y)
                number = get_number_end_pos(line, starter_pos)
                number_pos.add(number)


print(sum([int(n[0][3]) * int(n[1][3]) for n in [get_gear_ration(symbol, number_pos) for symbol in symbol_pos] if len(n) == 2]))