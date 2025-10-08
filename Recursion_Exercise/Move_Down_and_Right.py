Marinette has the ability to transform into Ladybug. She is stuck on a grid. 
Her initial location is at the top-left corner and tries to move to the bottom-right corner. 
However, she can only move either down or right at any point in time.

Write a program that prints the number of all possible unique paths that Marinette can take to reach the bottom-right corner.



def find_all_paths(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0
    if row == rows - 1 and col == cols - 1:
        return 1

    result = 0
    result += find_all_paths(row, col + 1, rows, cols)
    result += find_all_paths(row + 1, col, rows, cols)
    return result

rows = int(input())
cols = int(input())

print(find_all_paths(0, 0, rows, cols))
