from utils.utils import read_lines

def is_strictly_increasing_or_decreasing(report):
    increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def can_be_made_safe_by_removing_one(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_strictly_increasing_or_decreasing(modified_report):
            return True
    return False

lines = read_lines()

safe_count = 0

safe_count_with_elf_failsafe = 0

for line in lines:
    report = list(map(int, line.split()))
    if is_strictly_increasing_or_decreasing(report):
        safe_count += 1
    elif can_be_made_safe_by_removing_one(report):
        safe_count_with_elf_failsafe += 1

    safe_count_with_elf_failsafe += safe_count

print(f"Number of safe reports: {safe_count}")
print(f"Number of safe reports with elf failsafe: {safe_count_with_elf_failsafe}")