from collections import deque

nums = [int(x) for x in input().split()]

dp = [[0] * len(nums) for _ in range(2)]       
parent = [[None] * len(nums) for _ in range(2)]

dp[0][0] = dp[1][0] = 1

best_size = 1
best_row = 0
best_idx = 0

for current in range(1, len(nums)):
    current_number = nums[current]

    dp[0][current] = dp[1][current] = 1

    for prev in range(current - 1, -1, -1):
        prev_number = nums[prev]

        if current_number > prev_number and dp[1][prev] + 1 > dp[0][current]:
            dp[0][current] = dp[1][prev] + 1
            parent[0][current] = prev

        if current_number < prev_number and dp[0][prev] + 1 > dp[1][current]:
            dp[1][current] = dp[0][prev] + 1
            parent[1][current] = prev

    if dp[0][current] > best_size:
        best_size = dp[0][current]
        best_row = 0
        best_idx = current

    if dp[1][current] > best_size:
        best_size = dp[1][current]
        best_row = 1
        best_idx = current

result = deque()
while best_idx is not None:
    result.appendleft(nums[best_idx])
    best_idx = parent[best_row][best_idx]
    best_row = 1 if best_row == 0 else 0

print(*result, sep=" ")
