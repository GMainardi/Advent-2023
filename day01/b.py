def repalce_numbers(line: str) -> str:
    numbers = { 'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e', 'zero': 'z0o'}
    for number in numbers:
        if number in line:
            line = line.replace(number, numbers[number])
    return line

def get_line_digit(line: str) -> int:
    digits = [x for x in repalce_numbers(line) if x.isdigit()]
    return digits[0] + digits[-1]

with open('input.txt', 'r') as f:

    total = 0

    for line in f:
        total += int(get_line_digit(line.strip()))

    print(total)