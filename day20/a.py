HIGH = 'high'
LOW = 'low'

class Module():

    def __init__(self, description):
        self.name = description.split('->')[0][:-1]
        self.destinations = description.split('->')[1].replace(' ', '').split(',')
        pass

    def send_signal(self, input, signal):
        pass

    def __hash__(self) -> int:
        return hash(self.name)
    
    def __repr__(self) -> str:
        return f'{self.name} -> {self.destinations}'

class Broadcast(Module):

    def __init__(self, description):
        super().__init__(description)

    def send_signal(self, _, signal):
        return [(self.name, destination, signal) for destination in self.destinations]

class FlipFlop(Module):

    def __init__(self, description):
        super().__init__(description)
        self.state = False

    def send_signal(self, _, signal):
        if signal == HIGH:
            return []
        

        if not self.state:
            self.state = True
            return [(self.name, destination, HIGH) for destination in self.destinations]
        
        self.state = False
        return [(self.name, destination, LOW) for destination in self.destinations]

class Conjunction(Module):

    def __init__(self, description):
        super().__init__(description)
        self.connections = {}

    def add_connections(self, connection) -> None:
        self.connections[connection] = LOW

    def send_signal(self, input, signal):
        self.connections[input] = signal
        if all(signal == HIGH for signal in self.connections.values()):
            return [(self.name, destination, LOW) for destination in self.destinations]
        
        return [(self.name, destination, HIGH) for destination in self.destinations]

class FactoryModel():

    @staticmethod
    def create_model(description: str) -> Module:
        if description[0] == '%':
            return FlipFlop(description[1:])
        elif description[0] == '&':
            return Conjunction(description[1:])
        
        return Broadcast(description)
    
def update_conjuction(cirquit: dict[str, Module]) -> None:
    for name, module in cirquit.items():
        for connections in module.destinations:
            if connections not in cirquit:
                continue
            if isinstance(cirquit[connections], Conjunction):
                cirquit[connections].add_connections(name)

def push_button(cirquit: dict[str, Module]) -> None:
    
    queue = [('button', 'broadcaster', LOW)]

    signals = (0, 0)

    while queue:
        src, dest, signal = queue.pop(0)

        #print(f'{src} -{signal}-> {dest}')
        signals = (signals[0]+1, signals[1]) if signal == HIGH else (signals[0], signals[1]+1)

        if dest not in cirquit:
            continue

        queue.extend(cirquit[dest].send_signal(src, signal))

    return signals


with open('input.txt') as f:

    cirquit = {}
    for line in f.readlines():
        model = FactoryModel.create_model(line.strip())

        cirquit[model.name] = model

update_conjuction(cirquit)

total_signals = (0, 0)
for _ in range(1_000):

    cicle_signals = push_button(cirquit)
    total_signals = (total_signals[0] + cicle_signals[0], total_signals[1] + cicle_signals[1])

print(total_signals)
print(total_signals[0] * total_signals[1])