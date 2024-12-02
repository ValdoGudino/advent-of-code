from utils.utils import read_lines

def parse_game_line(line):
    game_data = line.split(': ')[1]

    group1, group2 = game_data.split(' | ')
    
    winning_numbers = list(map(int, group1.split()))
    scratch_numbers = list(map(int, group2.split()))
    
    return winning_numbers, scratch_numbers

def calculate_point_value(line):
    winning_numbers, scratch_numbers = parse_game_line(line)
    point_value = 0

    for number in scratch_numbers:
        if number in winning_numbers:
            if point_value == 0:
                point_value = 1
            else:
                point_value *= 2

    return point_value

def calculate_scatchcards_match(line):
    winning_numbers, scratch_numbers = parse_game_line(line)
    match = 0

    for number in scratch_numbers:
        if number in winning_numbers:
            match += 1

    return scratchcards_sum

def calculate_scratchcards_sum(lines):
    scratchcards_sum = 0

    for line in lines:
        scratchcards_sum += calculate_scatchcards_match(line)

    return scratchcards_sum

lines = read_lines()

point_value_sum = sum(calculate_point_value(line) for line in lines) 
print('Point value sum:', point_value_sum)

scratchcards_sum = calculate_scratchcards_sum(lines)