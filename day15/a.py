def hash(key: str) -> int:
    current_value = 0
    for char in key:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


with open('input.txt', 'r') as file:
    input = file.read().strip().split(',')

print(sum(map(lambda x: hash(x), input)))