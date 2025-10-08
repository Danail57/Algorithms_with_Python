def fibonacci(number):
    if number in [1, 2]:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)

number = int(input())
for i in range(1, number + 1):
    print(fibonacci(i))
