from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
dec = deque()
for i in range(T):
    com = list(input().split())
    if com[0] == "push_back":
        dec.append(int(com[1]))
    elif com[0] == "push_front":
        dec.appendleft(int(com[1]))
    elif com[0] == "pop_front":
        print(dec.popleft() if not len(dec)==0 else -1)
    elif com[0] == "pop_back":
        print(dec.pop() if not len(dec)==0 else -1)
    elif com[0] == "size":
        print(len(dec))
    elif com[0] == "empty":
        print(1 if len(dec)==0 else 0)
    elif com[0] == "front":
        print(dec[0] if len(dec) != 0 else -1)
    elif com[0] == "back":
        print(dec[-1] if len(dec) != 0 else -1)