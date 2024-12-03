import re

import utils.utils as utils

mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
do_pattern = r'do\(\)'
dont_pattern = r"don't\(\)"

def multiply_and_sum(string):
    matches = re.findall(mul_pattern, string)
    return sum(int(x) * int(y) for x, y in matches)

def multiply_and_sum_do_and_dont(string):
    parts = re.split(f'({mul_pattern}|{do_pattern}|{dont_pattern})', string)
    
    total_sum = 0
    mul_enabled = True
    
    for part in parts:
        if not part:
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

input_string = utils.read_string_from_file()

result = multiply_and_sum(input_string)
print("Total sum of multiplications:", result)

result = multiply_and_sum_do_and_dont(input_string)
print("Total sum of multiplications with do() and don't():", result)