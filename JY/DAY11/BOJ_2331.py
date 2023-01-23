import sys
A, P = sys.stdin.readline().split()
A = int(A)
P = int(P)

stack = [A]

while True:
    res = 0
    for i in str(stack[-1]): #제일 마지막에 있는 것이 계산할 대상이다.
        res += int(i) ** P
    if res in stack:
        while True:
            if res == stack.pop():
                sys.stdout.write(str(len(stack)))
                exit()
    else:
        stack.append(res)
        

