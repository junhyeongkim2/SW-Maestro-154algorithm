N = input()
stack = []
temp = False
result = 0

for i, n in enumerate(N):
    if n == "(":
        stack.append(n)
        temp = False
    else:
        m = stack.pop()
        if not temp: #(), 즉 레이져
            result += stack.count("(") #바로 파이프의 개수 셈. 생각하지 못 했던 부분
        else:
            result += 1
        temp = True

print(result)
