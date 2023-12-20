from math import lcm

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

    to_rx = ''
    for name, module in cirquit.items():
        for connections in module.destinations:
            if connections == 'rx':
                to_rx = name
                continue
            if isinstance(cirquit[connections], Conjunction):
                cirquit[connections].add_connections(name)

    return to_rx

def count_presses_periods(cirquit: dict[str, Module], to_rx) -> None:
    
    connections_periods = {c: -1 for c in cirquit[to_rx].connections.keys()}

    presses = 1

    queue = [('button', 'broadcaster', LOW)]


    while queue:
        src, dest, signal = queue.pop(0)

        if dest == to_rx:
            if signal == HIGH:
                if connections_periods[src] == -1:
                    connections_periods[src] = presses

            if all(p != -1 for p in connections_periods.values()):
                return connections_periods
            
        if dest == 'rx':
            if not len(queue):
                queue = [('button', 'broadcaster', LOW)]
                presses += 1
            continue

        queue.extend(cirquit[dest].send_signal(src, signal))


    return None

with open('input.txt') as f:

    cirquit = {}
    for line in f.readlines():
        model = FactoryModel.create_model(line.strip())

        cirquit[model.name] = model

to_rx = update_conjuction(cirquit)

periods = count_presses_periods(cirquit, to_rx)

print(lcm(*periods.values()))

    