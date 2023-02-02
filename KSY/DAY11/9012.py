n = int(input())

for _ in range(n):
    stack = []
    temp = False
    pses = input()
    for p in pses:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                temp = True
                break
            else:
                stack.pop()
    if temp or stack:
        print("NO")
    else:
        print("YES")
