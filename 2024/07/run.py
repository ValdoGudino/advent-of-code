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

def calculate_total_calibration(input_objects, ops, skip_z_values=None):
    total_calibration = 0
    skip_z_values = skip_z_values or set()
    for obj in input_objects:
        if obj.z in skip_z_values:
            continue
        if evaluate_expression(obj.values, obj.z, ops):
            total_calibration += obj.z
            skip_z_values.add(obj.z)
    return total_calibration, skip_z_values

input_objects = load_input()

# First calculation with '+' and '*'
ops = ['+', '*']
total_calibration, skip_z_values = calculate_total_calibration(input_objects, ops)
print(f"Total Calibration Result (without '||'): {total_calibration}")

# Second calculation with '+', '*', and '||', skipping already accounted z values
ops += ['||']
total_calibration_with_concat, _ = calculate_total_calibration(input_objects, ops, skip_z_values)
print(f"Total Calibration Result (with '||'): {total_calibration_with_concat}")

# Combined total calibration result
combined_total_calibration = total_calibration + total_calibration_with_concat
print(f"Combined Total Calibration Result: {combined_total_calibration}")