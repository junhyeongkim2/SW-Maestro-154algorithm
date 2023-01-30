#9012 괄호

import sys

n = int(input())

for i in range(n):
    stk = []
    arr = sys.stdin.readline()
    for s in arr:
        if s == '(':
            stk.append(s)
        elif s == ')':
            if len(stk) != 0:
                stk.pop()
            else:
                stk.append(s)
                break
                
    if len(stk) == 0 :
        print("YES")
    else:
        print("NO")
        