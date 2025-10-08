def explore_area(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if matrix[row][col] != '-':
        return 0

    matrix[row][col] = 'v'

    result = 1
    result += explore_area(row - 1, col, matrix)
    result += explore_area(row + 1, col, matrix)
    result += explore_area(row, col - 1, matrix)
    result += explore_area(row, col + 1, matrix)
    return result

rows = int(input())
cols = int(input())

matrix = [list(input()) for _ in range(rows)]

areas = []
for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col, matrix)
        if size == 0:
            continue
        areas.append((row, col, size))
print(f'Total areas found: {len(areas)}')

for idx, (row, col, size) in enumerate(sorted(areas, key=lambda a: -a[2])):
    print(f'Area #{idx + 1} at ({row}, {col}), size: {size}')

Example Layout                                 
4
9                                               
---*---*-
---*---*-
---*---*-
----*-*--
