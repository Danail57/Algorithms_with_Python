#1
n = int(input())
for x in range(1, n + 1):
    for y in range(1, n + 1):
        print(x, y)

#2
def number_vector(vector, index, n):
    if index == len(vector):
        print(*vector)
        return
    for number in range(1, n + 1):
        vector[index] = number
        number_vector(vector, index + 1, n)
n = int(input())
vector = [0] * n
number_vector(vector, 0, n)


#3
def number_vector(index, array):
    if index >= len(array):
        print(*array, sep=" ")
        return
    for number in range(1, len(array) + 1):
        array[index] = number
        number_vector(index + 1, array)
n = int(input())
array = [None] * n
number_vector(0, array)
