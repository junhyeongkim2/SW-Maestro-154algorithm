import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    n = list(input().split())

    if n[0] == 'push':
        stack.append(n[1])
    elif n[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif n[0] == 'size':
        print(len(stack))
    elif n[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif n[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
