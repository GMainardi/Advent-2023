class Rule:

    def __init__(self, rule) -> None:
        pass

    def evaluate(self, variables) -> str:
        pass

class defaultRule(Rule):

    def __init__(self, rule) -> None:
        self.out = rule

    def evaluate(self, _) -> str:
        return self.out
    
    def __str__(self) -> str:
        return self.out
    
class varRule(Rule):

    def __init__(self, rule) -> None:
        
        self.statement, self.out = rule.split(':')

        if '<' in self.statement:
            self.var, self.value = self.statement.split('<')

            def check(var) -> bool:
                value = int(self.value)
                return var < value
            
        elif '>' in self.statement:

            self.var, self.value = self.statement.split('>')

            def check(var) -> bool:
                value = int(self.value)
                return var > value
        
        self.compare = check

    def evaluate(self, variables) -> str:
        if self.compare(variables[self.var]):
            return self.out
        return None
    
    def __str__(self) -> str:
        return self.statement + ':' + self.out
    
class RuleFactory:

    @staticmethod
    def create(rule) -> Rule:
        if ':' in rule:
            return varRule(rule)
        else:
            return defaultRule(rule)


class Validator:

    def __init__(self, rules) -> None:
        self.name = rules.split('{')[0]
        self.rules = [RuleFactory.create(rule) for rule in rules[rules.index('{')+1:rules.index('}')].split(',')]

    def validate(self, variables) -> str:
        for rule in self.rules:
            out = rule.evaluate(variables)
            if out:
                return out
            
        return self.rules[-1].out

    def __repr__(self) -> str:
        return self.name + '{' + ','.join([str(rule) for rule in self.rules]) + '}'

def count_probs(part, ranges) -> int:

    global validations

    if part == 'A':
        result = 1
        for range in ranges.values():
            result *= range[1] - range[0] + 1
        return result

    if part == 'R':
        return 0

    total = 0

    for rule in validations[part].rules[:-1]:
        rule_range = ranges[rule.var]
        remain_ranges = ranges[rule.var]
        if '<' in rule.statement:
            rule_range = (rule_range[0], int(rule.value)-1)
            remain_ranges = (int(rule.value), remain_ranges[1])
        elif '>' in rule.statement:
            rule_range = (int(rule.value)+1, rule_range[1])
            remain_ranges = (remain_ranges[0], int(rule.value))

        new_ranges = ranges.copy()
        new_ranges[rule.var] = rule_range
        ranges[rule.var] = remain_ranges
        total += count_probs(rule.out, new_ranges)
    
    total += count_probs(validations[part].rules[-1].out, ranges)

    return total
        
    


with open('input.txt') as f:
    validations = {line.strip().split('{')[0]: Validator(line.strip()) for line in f.read().split('\n\n')[0].split('\n')}


init_ranges = {
    'x': (1, 4000),
    'm': (1, 4000),
    'a': (1, 4000),
    's': (1, 4000)
}

print(count_probs('in', init_ranges))