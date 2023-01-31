# import heapq
import sys
input = sys.stdin.readline

n = int(input())
queue = []
# heapq.heapify(queue)

for i in range(n):
    op = input().split()
    if op[0] == "push":
        queue.append(int(op[1]))
    elif op[0] == "pop":
        if queue:
            print(queue[0])
            del queue[0]
        else:
            print(-1)
    elif op[0] == "size":
        print(len(queue))
    elif op[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif op[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif op[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
