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

def calculate_checksum(parsed_list):
    checksum = 0
    for index, value in enumerate(parsed_list):
        if value != '.':
            checksum += int(value) * index
    return checksum

parsed_list = load_and_parse()
result_list = move_blocks(parsed_list)
checksum = calculate_checksum(result_list)
print(checksum)