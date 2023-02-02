#실패한 코드
N = input()
stack = []
raiser = []
pipe = []
result = 0
temp = False #'('였다면 False ')'였다면 True

for i, n in enumerate(N):
    if n == '(':
        stack.append(i)
        temp = False
    else:
        start = stack.pop() #stack에서 꺼내기
        if not temp: #(), 즉 레이져
            raiser.append(i)
        else: #연속 ))
            pipe.append((start, i))
        temp = True

for p in pipe:
    count = 0
    for r in raiser:
        if r > p[1]:
            break
        elif p[0] < r < p[1]:
            count += 1
    result += count + 1

print(result)