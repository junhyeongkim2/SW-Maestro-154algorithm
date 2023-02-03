import sys
input = sys.stdin.readline
T = int(input())


for _ in range(T):
    stack = []
    a = input()
    for i in a:
        if i == '(':
            stack.append(1)
        elif i == ')':
            if len(stack):
                stack.pop()
            else: # 스택에 괄호가 없을경우 NO
                print("NO")
                break
            #for-else문 break 실행 x, else문을 실행 
    else: 
        if len(stack) == 0: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
            print("YES")
        else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
            print("NO")