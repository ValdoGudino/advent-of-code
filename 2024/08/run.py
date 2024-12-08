from utils.utils import read_grid_from_file

def find_nodes(grid):
    nodes = {}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell.isalnum():
                if cell not in nodes:
                    nodes[cell] = []
                nodes[cell].append((i, j))
    return nodes
def calculate_antinodes(nodes, grid):
    antinodes = set()
    for positions in nodes.values():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                if grid[x1][y1] == grid[x2][y2]:  
                    dx, dy = x2 - x1, y2 - y1
                    k = 1
                    while True:
                        antinode1 = (x1 - k * dx, y1 - k * dy)
                        antinode2 = (x2 + k * dx, y2 + k * dy)
                        if 0 <= antinode1[0] < len(grid) and 0 <= antinode1[1] < len(grid[0]):
                            if antinode1 not in antinodes:
                                antinodes.add(antinode1)
                        if 0 <= antinode2[0] < len(grid) and 0 <= antinode2[1] < len(grid[0]):
                            if antinode2 not in antinodes:
                                antinodes.add(antinode2)
                        if not (0 <= antinode1[0] < len(grid) and 0 <= antinode1[1] < len(grid[0])) and not (0 <= antinode2[0] < len(grid) and 0 <= antinode2[1] < len(grid[0])):
                            break
                        k += 1
    return antinodes

def count_antinodes(grid):
    nodes = find_nodes(grid)
    antinodes = calculate_antinodes(nodes, grid)
    node_positions = {pos for positions in nodes.values() for pos in positions}
    total_antinodes = len(antinodes | node_positions)
    return total_antinodes



def parse_grid(input_str):
    return [list(line) for line in input_str.strip().split('\n')]

def print_grid_with_antinodes(grid, antinodes):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in antinodes:
                print('#', end='')
            else:
                print(grid[i][j], end='')
        print()

grid = read_grid_from_file()
grid = parse_grid(grid)

nodes = find_nodes(grid)
antinodes = calculate_antinodes(nodes, grid)

print_grid_with_antinodes(grid, antinodes)
print("Total antinodes:", count_antinodes(grid))