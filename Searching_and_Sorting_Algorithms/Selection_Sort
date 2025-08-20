#1
numbers = [int(x) for x in input().split()]

for index in range(len(numbers)):
    min_number = numbers[index]
    min_index = index
    for next_index in range(index + 1, len(numbers)):
        next_number = numbers[next_index]
        if next_number < min_number:
            min_number = next_number
            min_index = next_index
    numbers[index], numbers[min_index] = numbers[min_index], numbers[index]
print(*numbers, sep=" ")



#2
numbers = [int(x) for x in input().split()]
for i in range(len(numbers)):
    for j in range(1, len(numbers) - i):
        if numbers[j - 1] > numbers[j]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
print(*numbers, sep=" ")
