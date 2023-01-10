from collections import deque
import sys
imput = sys.stdin.readline

for i in range(int(input())):
    sentence = input()
    if sentence == '.':
        exit()
    dec = deque()
    for i in sentence:
        if  i == "(":
            dec.append(i)
        elif i == ")":
            if len(dec) == 0 or dec[-1] != "(":
                dec.append(-1)
                break
            else:
                dec.pop()
    if len(dec) == 0:
        print("YES")
    else:
        print("NO")