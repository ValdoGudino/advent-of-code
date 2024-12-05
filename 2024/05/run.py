from functools import cmp_to_key

from utils.utils import read_lines

def parse_input(lines):
    pairs = []
    sequences = []
    for line in lines:
        line = line.strip()
        if '|' in line:
            pair = tuple(map(int, line.split('|')))
            pairs.append(pair)
        elif ',' in line:
            sequence = list(map(int, line.split(',')))
            sequences.append(sequence)
    return pairs, sequences

def is_valid_subsequence(subsequence, pairs):
    index_map = {value: idx for idx, value in enumerate(subsequence)}
    for x, y in pairs:
        if x in index_map and y in index_map and index_map[x] > index_map[y]:
            print(f"Swapping {x} and {y}")
            subsequence[index_map[x]], subsequence[index_map[y]] = subsequence[index_map[y]], subsequence[index_map[x]]
            return False
    return True

def comparator(x, y, precedes_rules):
    if x in precedes_rules and y in precedes_rules[x]:
        return -1 
    if y in precedes_rules and x in precedes_rules[y]:
        return 1 
    return 0  

def sort_sequence(sequence, pairs):
    precedes_rules = {}
    for a, b in pairs:
        if a not in precedes_rules:
            precedes_rules[a] = set()
        precedes_rules[a].add(b)
    
    cmp = cmp_to_key(lambda x, y: comparator(x, y, precedes_rules))
    
    def recursive_sort(seq):
        sorted_seq = sorted(seq, key=cmp)
        if sorted_seq == seq:
            return sorted_seq
        return recursive_sort(sorted_seq)
    
    return recursive_sort(sequence)

def find_middle_of_sequence(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence is empty")
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        return sequence[length // 2 - 1]

def main():
    lines = read_lines()
    
    pairs, sequences = parse_input(lines)

    print(f"Sequences: {len(sequences)}")
    
    correct_middle_elements_sum = 0
    fixed_middle_elements_sum = 0
    fixed_sequences_count = 0

    for sequence in sequences:
        original_sequence = sequence.copy()
        was_fixed = False
        while not is_valid_subsequence(sequence, pairs):
            sequence = sort_sequence(sequence, pairs)
            was_fixed = True
        middle_element = find_middle_of_sequence(sequence)
        if was_fixed:
            print(f"Fixed sequence: {original_sequence} -> {sequence}")
            fixed_middle_elements_sum += middle_element
            fixed_sequences_count += 1
        else:
            correct_middle_elements_sum += middle_element
    
    print(f"Correct middle elements sum: {correct_middle_elements_sum}")
    print(f"Fixed middle elements sum: {fixed_middle_elements_sum}")
    print(f"Total sum: {correct_middle_elements_sum + fixed_middle_elements_sum}")
    print(f"Number of fixed sequences: {fixed_sequences_count}")

if __name__ == "__main__":
    main()