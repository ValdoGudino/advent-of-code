from utils.utils import read_grid_from_file


def parse_grid(input_str):
    return [list(line) for line in  input_str.strip().split('\n')]


def find_nodes(grid):
    nodes = {}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell.isalnum():
                if cell not in nodes:
                    nodes[cell] = []
                nodes[cell].append((i, j))
    return nodes

def calculate_antinodes(nodes):
    antinodes = set()
    for positions in nodes.values():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                if grid[x1][y1] == grid[x2][y2]:  
                    dx, dy = x2 - x1, y2 - y1
                    antinode1 = (x1 - dx, y1 - dy)
                    antinode2 = (x2 + dx, y2 + dy)
                    if 0 <= antinode1[0] < len(grid) and 0 <= antinode1[1] < len(grid[0]):
                        antinodes.add(antinode1)
                    if 0 <= antinode2[0] < len(grid) and 0 <= antinode2[1] < len(grid[0]):
                        antinodes.add(antinode2)
    return antinodes

def count_antinodes(grid):
    nodes = find_nodes(grid)
    antinodes = calculate_antinodes(nodes)
    return len(antinodes)

# Load grid from input.txt
grid = read_grid_from_file()
grid = parse_grid(grid)

print(count_antinodes(grid))