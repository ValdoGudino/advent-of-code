from utils.utils import read_grid_from_file

def parse_map(input_map):
    return [list(line) for line in input_map.strip().split('\n')]

def flood_fill(map, x, y, visited):
    stack = [(x, y)]
    region_type = map[x][y]
    area = 0
    perimeter = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        area += 1
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(map) and 0 <= ny < len(map[0]):
                if map[nx][ny] == region_type:
                    if (nx, ny) not in visited:
                        stack.append((nx, ny))
                else:
                    perimeter += 1
            else:
                perimeter += 1
    
    return area, perimeter

def calculate_total_price(input_map):
    map = parse_map(input_map)
    visited = set()
    total_price = 0
    
    for x in range(len(map)):
        for y in range(len(map[0])):
            if (x, y) not in visited:
                area, perimeter = flood_fill(map, x, y, visited)
                total_price += area * perimeter
    
    return total_price

input_map = read_grid_from_file()

print(calculate_total_price(input_map))