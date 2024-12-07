from utils.utils import read_lines
from itertools import product

class InputLine:
    def __init__(self, z, values):
        self.z = z
        self.values = values

    def __repr__(self):
        return f"InputLine(z={self.z}, values={self.values})"

def parse_line(line):
    parts = line.split(':')
    z = int(parts[0].strip())
    values = list(map(int, parts[1].strip().split()))
    return InputLine(z, values)

def load_input():
    lines = read_lines()
    input_objects = [parse_line(line) for line in lines]
    return input_objects

def evaluate_expression(values, z, ops):
    operators = list(product(ops, repeat=len(values)-1))
    
    for ops in operators:
        result = values[0]
        for i, op in enumerate(ops):
            if op == '+':
                result += values[i+1]
            elif op == '*':
                result *= values[i+1]
            elif op == '||':
                result = int(str(result) + str(values[i+1]))
        if result == z:
            return True
    return False

def calculate_total_calibration(input_objects, ops):
    total_calibration = 0
    for obj in input_objects:
        if evaluate_expression(obj.values, obj.z, ops):
            total_calibration += obj.z
    return total_calibration

input_objects = load_input()

ops = ['+', '*']
total_calibration = calculate_total_calibration(input_objects, ops)
print(f"Total Calibration Result: {total_calibration}")

ops += ['||']
total_calibration = calculate_total_calibration(input_objects, ops)
print(f"Total Calibration Result: {total_calibration}")