def read_grid_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def parse_grid(input_str):
    return [list(line) for line in input_str.strip().split('\n')]

def is_symbol(cell):
    return not cell.isdigit() and cell != '.'

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
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
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
    adjacent_numbers = set()

    for number, r, c in numbers:
        for i in range(len(number)):
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc + i
                    if 0 <= nr < rows and 0 <= nc < cols and is_symbol(grid[nr][nc]):
                        adjacent_numbers.add(number)
                        break

    return adjacent_numbers

# Read the grid from a file
file_path = 'input.txt'
input_str = read_grid_from_file(file_path)
grid = parse_grid(input_str)
adjacent_numbers = find_adjacent_numbers(grid)
print("Numbers adjacent to a symbol:", adjacent_numbers)
print("Sum of numbers adjacent to a symbol:", sum(map(int, adjacent_numbers)))