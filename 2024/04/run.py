from utils.utils import read_grid_from_file

def parse_grid(input_str):
    return [list(line) for line in  input_str.strip().split('\n')]

def search_and_mark_word(grid, word):
    count = 0
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0), 
        (1, 1), (1, -1), (-1, 1), (-1, -1) 
    ]

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not in_bounds(nx, ny) or grid[nx][ny] != word[i]:
                return False
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
        return True

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search_from(x, y, dx, dy):
                    count += 1

    return count

def count_a_bordered_by_mas(grid):
    count = 0
    rows, cols = len(grid), len(grid[0])
    marked = [[False] * cols for _ in range(rows)]

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_pattern(x, y):
        if not in_bounds(x, y) or grid[x][y] != 'A':
            return False
        # Check for "MAS" pattern
        if (in_bounds(x-1, y-1) and grid[x-1][y-1] == 'M' and
            in_bounds(x-1, y+1) and grid[x-1][y+1] == 'S' and
            in_bounds(x+1, y-1) and grid[x+1][y-1] == 'M' and
            in_bounds(x+1, y+1) and grid[x+1][y+1] == 'S'):
            marked[x][y] = True
            marked[x-1][y-1] = True
            marked[x-1][y+1] = True
            marked[x+1][y-1] = True
            marked[x+1][y+1] = True
            return True
        # Check for "SAM" pattern
        if (in_bounds(x-1, y-1) and grid[x-1][y-1] == 'S' and
            in_bounds(x-1, y+1) and grid[x-1][y+1] == 'S' and
            in_bounds(x+1, y-1) and grid[x+1][y-1] == 'M' and
            in_bounds(x+1, y+1) and grid[x+1][y+1] == 'M'):
            marked[x][y] = True
            marked[x-1][y-1] = True
            marked[x-1][y+1] = True
            marked[x+1][y-1] = True
            marked[x+1][y+1] = True
            return True
        
        # Check for mixed "MAS" and "SAM" patterns
        if (in_bounds(x-1, y-1) and grid[x-1][y-1] == 'M' and
            in_bounds(x-1, y+1) and grid[x-1][y+1] == 'M' and
            in_bounds(x+1, y-1) and grid[x+1][y-1] == 'S' and
            in_bounds(x+1, y+1) and grid[x+1][y+1] == 'S'):
            marked[x][y] = True
            marked[x-1][y-1] = True
            marked[x-1][y+1] = True
            marked[x+1][y-1] = True
            marked[x+1][y+1] = True
            return True
        
        if (in_bounds(x-1, y-1) and grid[x-1][y-1] == 'S' and
            in_bounds(x-1, y+1) and grid[x-1][y+1] == 'M' and
            in_bounds(x+1, y-1) and grid[x+1][y-1] == 'S' and
            in_bounds(x+1, y+1) and grid[x+1][y+1] == 'M'):
            marked[x][y] = True
            marked[x-1][y-1] = True
            marked[x-1][y+1] = True
            marked[x+1][y-1] = True
            marked[x+1][y+1] = True
            return True
        
        return False
        

    for x in range(1, rows-1):
        for y in range(1, cols-1):
            if check_pattern(x, y):
                count += 1

    return count

input_string = read_grid_from_file()

grid = parse_grid(input_string)
count = search_and_mark_word(grid, "XMAS")

print(f"Found XMAS: {count}")

grid = parse_grid(input_string)
count = count_a_bordered_by_mas(grid)

print(f"Found crosses: {count}")