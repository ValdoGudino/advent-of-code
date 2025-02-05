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

def evaluate_expression(values, z):
    operators = list(product(['+', '*', '||'], repeat=len(values)-1))
    
    for ops in operators:
        print(ops)
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

def calculate_total_calibration(input_objects):
    total_calibration = 0
    for obj in input_objects:
        if evaluate_expression(obj.values, obj.z):
            total_calibration += obj.z
    return total_calibration

# Example usage
if __name__ == "__main__":
    input_objects = load_input()
    total_calibration = calculate_total_calibration(input_objects)
    print(f"Total Calibration Result: {total_calibration}")