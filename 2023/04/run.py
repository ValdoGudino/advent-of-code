from utils.utils import read_lines

def parse_card_line(line):
    game_data = line.split(': ')[1]

    group1, group2 = game_data.split(' | ')
    
    winning_numbers = list(map(int, group1.split()))
    scratch_numbers = list(map(int, group2.split()))
    
    return winning_numbers, scratch_numbers

def calculate_point_value(line):
    winning_numbers, scratch_numbers = parse_card_line(line)
    point_value = 0

    for number in scratch_numbers:
        if number in winning_numbers:
            if point_value == 0:
                point_value = 1
            else:
                point_value *= 2

    return point_value

def calculate_matches(winning_numbers, scratch_numbers):
    matches = 0
    for number in scratch_numbers:
        if number in winning_numbers:
            matches += 1
    return matches

def calculate_total_scratchcards(lines):
    total_cards = len(lines)
    card_counts = [1] * total_cards  # Start with one of each card

    for i in range(total_cards):
        winning_numbers, scratch_numbers = parse_card_line(lines[i])
        matches = calculate_matches(winning_numbers, scratch_numbers)

        if matches > 0:
            for j in range(1, matches + 1):
                if i + j < total_cards:
                    card_counts[i + j] += card_counts[i]

    return sum(card_counts)

lines = read_lines()
point_value_sum = sum(calculate_point_value(line) for line in lines) 
print('Point value sum:', point_value_sum)

scratchcards_total = calculate_total_scratchcards(lines)
print("Scratchcards total:", scratchcards_total)