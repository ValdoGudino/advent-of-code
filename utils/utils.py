import os 

input_file_path = os.getcwd() + os.sep + os.environ['YEAR'] + os.sep + os.environ['DAY'] + os.sep + 'input.txt'

def read_grid_from_file():
    with open(input_file_path, 'r') as f:
        return f.read()

def read_lines():    
    with open(input_file_path, 'r') as f:
        return f.readlines()
