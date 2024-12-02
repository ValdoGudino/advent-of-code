print('Calculating distance between the two lists of numbers...')
first_list = []
second_list = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        num1, num2 = map(int, line.split())
        first_list.append(num1)
        second_list.append(num2)
        
first_list.sort()
second_list.sort()

distance = sum(abs(a - b) for a, b in zip(first_list, second_list))
print("Distance:", distance)

print('Calculating the similarity score between the two lists of numbers...')

similarity_score = sum(num * second_list.count(num) for num in first_list)
print("Similarity Score:", similarity_score)
