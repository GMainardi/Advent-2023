def line_to_int_list(line):
    return list(map(lambda x: int(x), line.strip().split(' ')))

def convert_seeds(dest_start, src_start, length, seeds):

    converted = set([])
    unmapped = seeds.copy()

    for seed in seeds:
        if seed >= src_start and seed <= src_start + length:
            unmapped.remove(seed)
            pos = seed - src_start
            seed = dest_start + pos
            converted.add(seed)
            

    return converted, unmapped

def plan_to_seed_map(plan):

    plan = plan.split('\n')[1:]

    seed_map = [line_to_int_list(line) for line in plan]

    return seed_map


with open('input.txt', 'r') as f:
    lines = f.readlines()

plan = ''.join(lines).split('\n\n')

seeds = line_to_int_list(plan[0].split(':')[1])

almanac = [plan_to_seed_map(p) for p in plan[1:]]

for seed_map in almanac:

    converted = set([])
    for line in seed_map:
        dest_start, src_start, length = line
        new_conv, unmapped = convert_seeds(dest_start, src_start, length, seeds)
        converted = converted.union(new_conv)
        seeds = unmapped.copy()

    seeds = converted.union(seeds)
    
print(min(seeds))