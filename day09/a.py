def predict_value(history):


    if all([x == 0 for x in history]):
        return 0
    
    diff_list = [history[i] - history[i-1] for i in range(1, len(history))]
    last_value = history[-1]
    target = predict_value(diff_list)

    return target + last_value

def line_to_int_list(line):
    return [int(x) for x in line.strip().split()]

with open('input.txt', 'r') as f:
    data = f.readlines()

print(sum([predict_value(line_to_int_list(line)) for line in data]))
