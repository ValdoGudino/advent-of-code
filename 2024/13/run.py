from utils.utils import read_string_from_file
import re

def find_intersection(a1, a2, b1, b2, X, Y):
    a1_times_b2 = a1 * b2
    x_times_b2 = X * b2

    a2_times_b1 = a2 * b1
    y_times_b2 = Y * b1

    a = (x_times_b2 - y_times_b2) / (a1_times_b2 - a2_times_b1)

    b = (Y - a2 * a) / b2

    if not a.is_integer() or not b.is_integer():
        raise ValueError("The solution is not an integer.")

    return a, b

def parse_input(input_str):
    pattern = re.compile(r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)')
    matches = pattern.findall(input_str)
    return [(int(a1), int(b1), int(a2), int(b2), int(X), int(Y)) for a1, b1, a2, b2, X, Y in matches]

input_str = read_string_from_file()

test_cases = parse_input(input_str)

def solve(increment=False):
    min_tokens = 0
    for a1, b1, a2, b2, X, Y in test_cases:
        try:
            if increment:
                X += 10_000_000_000_000
                Y += 10_000_000_000_000
            a, b = find_intersection(a1, b1, a2, b2, X, Y)
            min_tokens += int(3 * a + b)
        except ValueError:
            continue        

    print("Solution:", min_tokens)

solve()
solve(True)