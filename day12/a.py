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

def count_matches(s, t):

    if sum(t) > len(s):
        return 0
    
    if s is None:
        return 0

    if len(s) == 0:
        return 1
    
    if s[-1] == '.':
        return count_matches(s[:-1], t)
    
    if s[-1] == '#':
        return eat_chunk(s, t)

    return count_matches(s[:-1], t) + eat_chunk(s, t)
        

    
with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


total = 0
for line in lines:
    test_string, test_list = line.split()
    test_list = [int(x) for x in test_list.split(',')]
    total += count_matches(test_string, test_list)

print(total)