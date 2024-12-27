from functools import cache
from math import log, floor

@cache
def get_span(stone, blinks):
    if blinks == 0:
        return 1
    elif stone == 0:
        return get_span(1, blinks - 1)  
    elif (digits := (floor(log(stone, 10)) + 1)) % 2 < 1:
        left = stone // 10 ** (digits // 2)
        right = stone % 10 ** (digits // 2)
        return get_span(left, blinks - 1) + get_span(right , blinks - 1)
    else:
        return get_span(stone * 2024, blinks - 1)

# Example usage
initial_stones = [1750884, 193, 866395, 7, 1158, 31, 35216, 0]
blinks = 25

print(sum(get_span(stone, blinks) for stone in initial_stones)) 


blinks = 75
print(sum(get_span(stone, blinks) for stone in initial_stones)) 