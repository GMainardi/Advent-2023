def line_to_int_list(line):
    return list(map(lambda x: int(x), line.strip().split(' ')))

def plan_to_seed_map(plan):

    plan = plan.split('\n')[1:]

    seed_map = [line_to_int_list(line) for line in plan]

    return seed_map

def get_overlap(start1, end1, start2, end2):

    first, overlap, last = None, None, None

    if start1 <= end2 and start2 <= end1:

        if start2 < start1:
            first = (start2, start1-start2)

            if end2 < end1:
                overlap = (start1, end2-start1)
            else:
                overlap = (start1, end1-start1)
                last = (end1, end2-end1)
        else:
            
            if end1 < end2:
                overlap = (start2, end1-start2)
                last = (end1, end2-end1)
            else:
                overlap = (start2, end2-start2)

    return first, overlap, last

def convert_seeds(dest_start, src_start, length, seeds):

    converted = set([])
    unmapped = seeds.copy()


    for seed in seeds:

        seed_start, seed_length = seed

        
        overlap = get_overlap(
            src_start, 
            src_start+length, 
            seed_start, 
            seed_start+seed_length
        )

        first, overlap, last = overlap
        if overlap is None:
            continue

        unmapped.remove(seed)
        
        if first is not None:
            unmapped.add(first)

        if last is not None:
            unmapped.add(last)

        overlap_start, overlap_length = overlap
        convert_start = dest_start + (overlap_start - src_start)
        converted.add((convert_start, overlap_length))

    return converted, unmapped


with open('input.txt', 'r') as f:
    lines = f.readlines()

plan = ''.join(lines).split('\n\n')

seeds_range = line_to_int_list(plan[0].split(':')[1])

it = iter(seeds_range)
seeds = set(zip(it, it))

almanac = [plan_to_seed_map(p) for p in plan[1:]]

for seed_map in almanac:
    converted = set([])
    for line in seed_map:
        dest_start, src_start, length = line
        new_conv, unmapped = convert_seeds(dest_start, src_start, length, seeds)
        converted = converted.union(new_conv)
        seeds = unmapped.copy()
    
    seeds = converted.union(seeds)

print(min(seeds)[0])