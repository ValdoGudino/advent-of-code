from utils.utils import read_grid_from_file

def parse_grid(input_str):
    return [list(line) for line in input_str.strip().split('\n')]

def is_symbol(cell):
    return cell != '.' and not cell.isdigit()

def find_numbers(grid):
    rows = len(grid)
    cols = len(grid[0])
    numbers = []
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        stack = [(r, c)]
        num = ''
        while stack:
            x, y = stack.pop()
            if 0 <= x < rows and 0 <= y < cols and grid[x][y].isdigit() and not visited[x][y]:
                visited[x][y] = True
                num += grid[x][y]
                for dx, dy in [(0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny].isdigit() and not visited[nx][ny]:
                        stack.append((nx, ny))
        return num

    for r in range(rows):
        for c in range(cols):
            if grid[r][c].isdigit() and not visited[r][c]:
                number = dfs(r, c)
                if number:
                    numbers.append((number, r, c))
    
    return numbers

def find_adjacent_numbers(grid):
    rows = len(grid)
    cols = len(grid[0])
    numbers = find_numbers(grid)
    adjacent_numbers = []
    coordinate_matched = set()

    for number, r, c in numbers:
        for i in range(len(number)):
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc + i
                    if 0 <= nr < rows and 0 <= nc < cols and is_symbol(grid[nr][nc]) and (r, c) not in coordinate_matched:
                        coordinate_matched.add((r, c))
                        adjacent_numbers.append(number)    
                        break
                    
    return adjacent_numbers

def find_symbol_coordinates(grid, symbol):
    rows = len(grid)
    cols = len(grid[0])
    coordinates = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == symbol:
                coordinates.append((r, c))

    return coordinates

def find_adjacent_pairs_for_gears(grid):
    rows = len(grid)
    cols = len(grid[0])
    numbers = find_numbers(grid)
    adjacent_pairs = []

    # Find all '*' coordinates
    gear_coordinates = find_symbol_coordinates(grid, '*')

    for r, c in gear_coordinates:
        adjacent_numbers = set()
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    for number, nr_num, nc_num in numbers:
                        if (nr_num == nr and nc_num == nc) or (nr_num == nr and nc_num <= nc < nc_num + len(number)):
                            adjacent_numbers.add(number)
        
        # If exactly two numbers are adjacent to the '*', add the pair to the result
        if len(adjacent_numbers) == 2:
            adjacent_pairs.append(tuple(adjacent_numbers))

    return adjacent_pairs

# Read the grid from a file
input_str = read_grid_from_file()
grid = parse_grid(input_str)
adjacent_numbers = find_adjacent_numbers(grid)
print("Sum of numbers adjacent to a symbol:", sum(map(int, adjacent_numbers)))

adjacent_pairs = find_adjacent_pairs_for_gears(grid)
sum_adjacent_pairs = sum([int(a) * int(b) for a, b in adjacent_pairs])
print('Sum of all gear ratios:', sum_adjacent_pairs)