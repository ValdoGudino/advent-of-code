from utils.utils import read_string_from_file
from collections import Counter

import re

width = 101
height = 103

def run(SECS=100):
    input_str = read_string_from_file()

    robots = []
    pattern = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
    for line in input_str.strip().split('\n'):
        match = pattern.match(line)
        if match:
            px, py, vx, vy = map(int, match.groups())
            robots.append({"p": (px, py), "v": (vx, vy)})
        
    for robot in robots:
        px, py = robot["p"]
        vx, vy = robot["v"]
        px = (px + vx * SECS) % width
        py = (py + vy * SECS) % height
        robot["p"] = (px, py)

    if SECS != 100:
        locations = [robot["p"] for robot in robots]
        grid = Counter(locations)

        for r in range(width):
            print("".join(str(grid.get((r, c), ".")) for c in range(height)))
        return 
    
    quadrant_counts = [0, 0, 0, 0]

    for robot in robots:
        px, py = robot["p"]
        if px == width // 2 or py == height // 2:
            continue
        if px < width // 2 and py < height // 2:
            quadrant_counts[0] += 1
        elif px >= width // 2 and py < height // 2:
            quadrant_counts[1] += 1
        elif px < width // 2 and py >= height // 2:
            quadrant_counts[2] += 1
        elif px >= width // 2 and py >= height // 2:
            quadrant_counts[3] += 1

    safety_factor = quadrant_counts[0] * quadrant_counts[1] * quadrant_counts[2] * quadrant_counts[3]

    print("Safety Factor:", safety_factor)


# last = 0
# for i in range(0, 100):
#     if i == 0:
#         last = 23
#     else:
#         last += width
#     print("Last:", last)
#     run(last)
#     print()



run(6285)
run(100)