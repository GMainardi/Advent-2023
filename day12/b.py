from functools import cache

def get_chunk(s, n):
    end = s[-n:]

    if any(c == '.' for c in end):
        return None
    
    return s[:-n]


def eat_chunk(s, t):

    if len(t) == 0:
            return 0
        
    to_eat = t[-1]
    chunk = get_chunk(s, to_eat)

    if chunk is None or (len(chunk) and chunk[-1] == '#'):
        return 0
    
    return count_matches(chunk[:-1], t[:-1])

@cache
def count_matches(s, t):

    if sum(t) + len(t) - 1 > len(s):
        return 0
    
    if len(s) == 0:
        return 1
    
    match s[-1]:
        case '.':
            return count_matches(s[:-1], t)
        case '#':
            return eat_chunk(s, t)
        case _:
            return count_matches(s[:-1], t) + eat_chunk(s, t)
        

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

total = 0
for line in lines:
    springs, test_list = line.split()

    springs += '?'
    springs = springs * 5
    springs = springs[:-1]

    test_list = [int(x) for x in test_list.split(',')] * 5
    total += count_matches(springs, tuple(test_list))


print(total)