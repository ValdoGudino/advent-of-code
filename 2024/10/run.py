from utils.utils import read_string_from_file
from collections import deque

def parse_map(input_str):
    return [list(map(int, line)) for line in input_str.strip().split('\n')]

def find_trailheads(map_data):
    trailheads = []
    for r in range(len(map_data)):
        for c in range(len(map_data[0])):
            if map_data[r][c] == 0:
                trailheads.append((r, c))
    return trailheads

def bfs(map_data, start):
    rows, cols = len(map_data), len(map_data[0])
    queue = deque([start])
    visited = set([start])
    reachable_nines = set()
    
    while queue:
        r, c = queue.popleft()
        if map_data[r][c] == 9:
            reachable_nines.add((r, c))
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if map_data[nr][nc] == map_data[r][c] + 1:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
    
    return len(reachable_nines)

def dfs(map_data, r, c, visited):
    rows, cols = len(map_data), len(map_data[0])
    if map_data[r][c] == 9:
        return 1
    
    visited.add((r, c))
    count = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
            if map_data[nr][nc] == map_data[r][c] + 1:
                count += dfs(map_data, nr, nc, visited)
    visited.remove((r, c))
    return count

def calculate_total_score_bfs(map_data):
    trailheads = find_trailheads(map_data)
    total_score = 0
    for trailhead in trailheads:
        total_score += bfs(map_data, trailhead)
    return total_score

def calculate_total_score_dfs(map_data):
    trailheads = find_trailheads(map_data)
    total_score = 0
    for trailhead in trailheads:
        total_score += dfs(map_data, trailhead[0], trailhead[1], set())
    return total_score

input_str = read_string_from_file()
map_data = parse_map(input_str)
total_score = calculate_total_score_bfs(map_data)
print(total_score) 

total_score = calculate_total_score_dfs(map_data)
print(total_score) 