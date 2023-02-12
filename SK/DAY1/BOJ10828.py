# Input
n = int(input())

# Define variables
stack = []

# Algorithm
for _ in range(n):
    command_line = input().split()
    command = command_line[0]

    if command == "push":
        value = command_line[1]
        stack.append(value)
    elif command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == "top":
        print(stack[-1])