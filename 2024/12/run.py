from utils.utils import read_grid_from_file

from shapely import box, MultiPolygon
from collections import defaultdict

shapes = defaultdict(MultiPolygon)

def parse_grid(input_str):
    return [list(line) for line in  input_str.strip().split('\n')]

input = parse_grid(read_grid_from_file())
for r, line in enumerate(input):
    for c, color in enumerate(line):
        shapes[color] = shapes[color].union( box(r, c, r + 1, c + 1) )

perimeter_calculation = 0
sides_calculation = 0
for color, polys in shapes.items():
    for poly in polys.geoms if hasattr(polys, "geoms") else [polys]:
        perimeter_calculation += int(poly.area * poly.length)
        boundary = poly.boundary.normalize().simplify(0.0)
        if boundary.is_ring:
            sides_calculation += int(poly.area * (len(boundary.coords) - 1))
        else:  
            for line in boundary.geoms:
                sides_calculation += int(poly.area * (len(line.coords) - 1))

print(f"Cost for perimeter calculation: {perimeter_calculation}")
print(f"Cost for sides calculation: {sides_calculation}")