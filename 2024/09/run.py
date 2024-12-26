from utils.utils import read_string_from_file

def load_and_parse():
    input_str = read_string_from_file()
    
    data = [int(x) for x in input_str]
    result = []
    file_id = 0
    
    for i in range(len(data)):
        if i % 2 == 0:
            result.extend([str(file_id)] * data[i])
            file_id += 1
        else:
            result.extend(['.'] * data[i])
    
    return result

def move_blocks(parsed_list):
    left_index = 0
    right_index = len(parsed_list) - 1
    
    while left_index < right_index:
        while left_index < len(parsed_list) and parsed_list[left_index] != '.':
            left_index += 1
        while right_index >= 0 and parsed_list[right_index] == '.':
            right_index -= 1
        
        if left_index < right_index:
            parsed_list[left_index], parsed_list[right_index] = parsed_list[right_index], parsed_list[left_index]
            left_index += 1
            right_index -= 1
    
    return parsed_list

def find_file_blocks(parsed_list):
    blocks = []
    i = 0
    while i < len(parsed_list):
        if parsed_list[i].isdigit():
            start = i
            while i < len(parsed_list) and parsed_list[i] == parsed_list[start]:
                i += 1
            blocks.append((parsed_list[start], start, i - start))
        else:
            i += 1
    return blocks

def find_free_spaces(parsed_list):
    free_spaces = []
    i = 0
    while i < len(parsed_list):
        if parsed_list[i] == '.':
            start = i
            while i < len(parsed_list) and parsed_list[i] == '.':
                i += 1
            free_spaces.append((start, i - start))
        else:
            i += 1
    return free_spaces

def move_whole_blocks(parsed_list):
    blocks = find_file_blocks(parsed_list)
    free_spaces = find_free_spaces(parsed_list)
    
    for block in reversed(blocks):
        block_char, block_start, block_length = block
        for space in free_spaces:
            space_start, space_length = space
            if space_length >= block_length and space_start < block_start:
                parsed_list[space_start:space_start + block_length] = [block_char] * block_length
                parsed_list[block_start:block_start + block_length] = ['.'] * block_length
                free_spaces = find_free_spaces(parsed_list)
                break

    return parsed_list

def calculate_checksum(parsed_list):
    checksum = 0
    for index, value in enumerate(parsed_list):
        if value != '.':
            checksum += int(value) * index
    return checksum

parsed_list = load_and_parse()
result_list = move_blocks(parsed_list.copy())
checksum = calculate_checksum(result_list)
print(checksum)

whole_result_list = move_whole_blocks(parsed_list.copy())
whole_checksum = calculate_checksum(whole_result_list)
print(whole_checksum)