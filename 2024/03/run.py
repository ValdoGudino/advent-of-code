import re

import utils.utils as utils

def multiply_and_sum(string):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, string)
    
    total_sum = 0
    
    for match in matches:
        x, y = map(int, match)
        total_sum += x * y
    
    return total_sum

def multiply_and_sum_do_and_dont(string):
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r"don't\(\)"
    
    parts = re.split(f'({mul_pattern}|{do_pattern}|{dont_pattern})', string)
    
    total_sum = 0
    mul_enabled = True
    
    for part in parts:
        if part is None or part.strip() == '':
            continue
        if re.match(do_pattern, part):
            mul_enabled = True
        elif re.match(dont_pattern, part):
            mul_enabled = False
        elif mul_enabled and re.match(mul_pattern, part):
            match = re.match(mul_pattern, part)
            x, y = map(int, match.groups())
            total_sum += x * y
    
    return total_sum

# Example usage
input_string = utils.read_grid_from_file()
result = multiply_and_sum(input_string)
print("Total sum of multiplications:", result)
result = multiply_and_sum_do_and_dont(input_string)
print("Total sum of multiplications with do() and don't():", result)