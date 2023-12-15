class HashMap:

    def __hash(key: str) -> int:
        current_value = 0
        for char in key:
            current_value += ord(char)
            current_value *= 17
            current_value %= 256
        return current_value

    def __init__(self, size: int = 256):
        self.size = size
        self.map = [None] * size

    def add(self, key: str, value: str):
        hash = HashMap.__hash(key)

        if self.map[hash] is None:
            self.map[hash] = [(key, value)]
        else:
            for idx, (k, _) in enumerate(self.map[hash]):
                if k == key:
                    self.map[hash][idx] = (key, value)
                    return
                
            self.map[hash].append((key, value))

    def remove(self, key: str):
        hash = HashMap.__hash(key)

        if self.map[hash] is None:
            return

        for idx, (k, _) in enumerate(self.map[hash]):
            if k == key:
                del self.map[hash][idx]
                if len(self.map[hash]) == 0:
                    self.map[hash] = None
                return
    
    def __focal_len_power(self, idx: int) -> int:
        return sum(
            map(
                lambda x: x[1][1] * (x[0] +1), 
                enumerate(self.map[idx])
                )
            )

    def get_focal_power(self) -> int:
        return sum(
            map(
                lambda x: (x+1) * self.__focal_len_power(x), 
                [box_idx 
                 for box_idx in range(self.size) 
                    if self.map[box_idx] is not None
                    ]
                )
            )
    
    def __repr__(self) -> str:
        string = ''
        for idx, box in enumerate(self.map):
            if box is None:
                continue

            string += f'Box [{idx}]: {box}\n'

        return string


with open('input.txt', 'r') as file:
    input = file.read().strip().split(',')

hashmap = HashMap()

for line in input:

    if '=' in line:
        key, value = line.split('=')
        hashmap.add(key, int(value))
    elif '-' in line:
        key = line[:-1]
        hashmap.remove(key)
    else:
        exit(0)

print(hashmap.get_focal_power())
