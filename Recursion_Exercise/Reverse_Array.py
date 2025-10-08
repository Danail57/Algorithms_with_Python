#1
numbers = [int(x) for x in input().split()]
numbers.reverse()
print(*numbers)


#2
numbers = [int(x) for x in input().split()]
print(*numbers[::-1])
