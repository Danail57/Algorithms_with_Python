#1
n = int(input())
def calc_fib(n):
    if n <= 2:
        return 1
    return calc_fib(n - 1) + calc_fib(n - 2)
print(calc_fib(n))


#2 - Optimized variant by using Memoization

n = int(input())

def calc_fib(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    result = calc_fib(n - 1, memo) + calc_fib(n - 2, memo)
    memo[n] = result
    return result

print(calc_fib(n, {}))
