def binary_search(numbers, target_number):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid_index = (left + right) // 2
        mid_element = numbers[mid_index]
        if mid_element == target_number:
            return mid_index
        if target_number > mid_element:
            left = mid_index + 1
        else:
            right = mid_index - 1
    return -1

numbers = [int(x) for x in input().split()]
target_number = int(input())
print(binary_search(numbers, target_number))
