def get_line_digit(line: str) -> int:
    digits = [x for x in line if x.isdigit()]
    return digits[0] + digits[-1]

with open('input.txt', 'r') as f:

    total = 0

    for line in f:
        total += int(get_line_digit(line))

    print(total)