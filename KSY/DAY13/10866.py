import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
deq = deque()

for _ in range(n):
    query = list(input().split())

    if query[0] == 'push_back':
        deq.append(int(query[1]))
    elif query[0] == 'push_front':
        deq.appendleft(int(query[1]))
    elif query[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif query[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)
    elif query[0] == 'size':
        print(len(deq))
    elif query[0] == 'empty':
        if not deq:
            print(1)
        else:
            print(0)
    elif query[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif query[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)