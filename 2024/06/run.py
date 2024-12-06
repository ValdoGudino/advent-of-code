from utils.utils import read_grid_from_file

directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

def parse_grid(input_str):
    return [list(line) for line in input_str.strip().split('\n')]


def out_of_bounds(x, y, grid):
    return not (0 <= x < len(grid) and 0 <= y < len(grid[0]))

def simulate_guard_movement(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in directions:
                x, y = i, j
                grid[x][y] = '.'
                direction = cell
                break

    visited = set()
    obstacles_encountered = {}
    while not out_of_bounds(x, y, grid):
        visited.add((x, y))

        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        
        if out_of_bounds(nx, ny, grid): 
            break
        elif grid[nx][ny] == '.':
            x, y = nx, ny
        else:
            if (nx, ny, direction) in obstacles_encountered:
                return 0, True
            obstacles_encountered[(nx, ny, direction)] = True
            direction = turns[direction]
    
    return len(visited), False

def count_obstacle_positions(grid):
    count = 0

    initial_x, initial_y = None, None
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in directions:
                initial_x, initial_y = i, j
                break

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.' and (i, j) != (initial_x, initial_y):
                grid_copy = [row[:] for row in grid]  # Create a deep copy of the grid
                grid_copy[i][j] = '#'
                _, is_loop = simulate_guard_movement(grid_copy)
                if is_loop:
                    count += 1
                    print("Obstacle at position", i, j, "causes a loop")
                grid_copy[i][j] = '.'
    return count

print("Starting the guard simulation...")
input_string = read_grid_from_file()
grid = parse_grid(input_string)
grid_copy = [row[:] for row in grid]
distinct_coordinates, is_loop = simulate_guard_movement(grid_copy)
print("The number of distinct coordinates visited by the guard is:", distinct_coordinates)

grid_copy = [row[:] for row in grid]
obstacle_positions = count_obstacle_positions(grid_copy)
print("The number of ways to add an obstacle to get the guard stuck in a loop is:", obstacle_positions)