class Rule:

    def __init__(self, rule) -> None:
        pass

    def evaluate(self, variables) -> str:
        pass

class defaultRule(Rule):

    def __init__(self, rule) -> None:
        self.rule = rule

    def evaluate(self, _) -> str:
        return self.rule
    
    def __str__(self) -> str:
        return self.rule
    
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

def evaluate(variables, validations):
    validator = 'in'
    while True:
        eval = validations[validator].validate(variables)
        if eval in ('R', 'A'):
            return eval
        validator = eval

def parse_vars(line) -> dict:
    return {var.split('=')[0]: int(var.split('=')[1]) for var in line[1:-1].split(',')}

with open('input.txt') as f:
    rules, variables = f.read().split('\n\n')
    validations = {line.strip().split('{')[0]: Validator(line.strip()) for line in rules.split('\n')}
    variables = [parse_vars(line) for line in variables.split('\n')]

total = 0
for variables in variables:
    if evaluate(variables, validations) == 'A':
        total += sum(variables.values())

print(total)