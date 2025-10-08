def merge_arrays(left, right):
    result = [None] * (len(left) + len(right))
    left_index = 0
    right_index = 0
    result_index = 0



    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result[result_index] = left[left_index]
            left_index += 1
        else:
            result[result_index] = right[right_index]
            right_index += 1
        result_index += 1

    while left_index < len(left):
        result[result_index] = left[left_index]
        left_index += 1
        result_index += 1

    while right_index < len(right):
        result[result_index] = right[right_index]
        right_index += 1
        result_index += 1
    return result

def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers

    mid_index = len(numbers) // 2
    left = numbers[:mid_index]
    right = numbers[mid_index:]

    return merge_arrays(merge_sort(left), merge_sort(right))

numbers = [int(x) for x in input().split()]
result = merge_sort(numbers)
print(*result, sep=" ")
