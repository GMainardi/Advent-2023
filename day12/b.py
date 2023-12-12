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

mem = {}
def count_matches(s, t):
    
    if (s, t) in mem:
        return mem[(s, t)]
    
    if sum(t) > len(s):
        mem[(s, t)] = 0
        return mem[(s, t)]

    if s is None:
        mem[(s, t)] = 0
        return mem[(s, t)]

    if len(s) == 0:
        mem[(s, t)] = 1
        return mem[(s, t)]

    
    if s[-1] == '.':
        mem[(s, t)] = count_matches(s[:-1], t)
        return mem[(s, t)]

    
    if s[-1] == '#':
        mem[(s, t)] = eat_chunk(s, t)
        return mem[(s, t)]

    mem[(s, t)] = count_matches(s[:-1], t) + eat_chunk(s, t)
    return mem[(s, t)]
        

    
with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


total = 0
for line in lines:
    test_string, test_list = line.split()
    test_string += '?'
    test_string = test_string * 5
    test_string = test_string[:-1]

    test_list = [int(x) for x in test_list.split(',')] * 5
    total += count_matches(test_string, tuple(test_list))


print(total)