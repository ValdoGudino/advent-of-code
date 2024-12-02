# Dictionary to map spelled-out digits to their numeric equivalents
digit_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def parse_digits_to_number(digits):
    # Get the first and last digit
    if len(digits) > 0:
        first_digit = digits[0]
        last_digit = digits[-1]
        return int(first_digit + last_digit)
    else:
        return None  # Not enough digits to form a number

def part_one(s):
    # Extract digits from the string
    digits = [char for char in s if char.isdigit()]
    return parse_digits_to_number(digits)

def part_two(input_string):
    def find_first_digit(s):
        for i in range(len(s)):
            if s[i].isdigit():
                return s[i]
            for word, digit in digit_map.items():
                if s[i:i+len(word)] == word:
                    return digit
        return None
    
    def find_last_digit(s):
        for i in range(len(s)-1, -1, -1):
            if s[i].isdigit():
                return s[i]
            for word, digit in digit_map.items():
                if s[i-len(word)+1:i+1] == word:
                    return digit
        return None
    
    first_digit = find_first_digit(input_string)
    last_digit = find_last_digit(input_string)
    
    digits = [first_digit, last_digit] if first_digit and last_digit else []
    return parse_digits_to_number(digits)

with open('input.txt', 'r') as f:
    lines = f.readlines()

part_one_sum = sum([part_one(line) for line in lines])
part_two_sum = sum([part_two(line) for line in lines])

print("Part One Sum:", part_one_sum)
print("Part Two Sum:", part_two_sum)