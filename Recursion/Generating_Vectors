def generating_vectors(vector, index):
    if index >= len(vector):
        print(*vector, sep='')
        return
    for number in range(2):
        vector[index] = number
        generating_vectors(vector, index + 1)

n = int(input())
vector = [0] * n
generating_vectors(vector, 0)
