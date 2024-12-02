max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14   
}

def parse_game_line(line):
    # Split the line by the game identifier
    game_number, game_data = line.split(': ')
    
    # Split the game data by ';' to get each turn
    turns = game_data.split('; ')
    
    # Initialize a list to store the colors for each turn
    parsed_turns = []
    
    # Iterate over each turn
    for turn in turns:
        # Split the turn by ', ' to get each color and count
        color_counts = turn.split(', ')
        
        # Initialize a dictionary to store the colors and counts for this turn
        turn_colors = {}
        
        # Iterate over each color and count
        for color_count in color_counts:
            # Split the color and count
            count, color = color_count.split(' ')
            # Add the color and count to the turn_colors dictionary
            turn_colors[color] = int(count)
        
        # Append the turn_colors dictionary to the parsed_turns list
        parsed_turns.append(turn_colors)
    
    return int(game_number.split(' ')[1]), parsed_turns

def is_game_possible(parsed_game):
    for turn in parsed_game:
        for color, count in turn.items():
            if count > max_cubes.get(color, 0):
                return False
    return True

def get_power(parsed_game):
    min_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0   
    }
    for turn in parsed_game:
        for color, count in turn.items():
            if count > min_cubes.get(color):
                min_cubes[color] = count


    # Calculate the product of the minimum counts
    power = 1
    for count in min_cubes.values():
        power *= count
    return power
    

with open('input.txt', 'r') as f:
    lines = f.readlines()

possible_sum = 0
sum_of_power = 0

for line in lines:
    game_number, parsed_game = parse_game_line(line.strip())
    if is_game_possible(parsed_game):
       possible_sum += game_number

    sum_of_power += get_power(parsed_game)
    
print("Possible Sum: ", possible_sum)
print("Sum of Power: ", sum_of_power)
