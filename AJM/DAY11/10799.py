#10799 쇠막대기
arr = str(input())
stk = []
answer = 0

for i in range(len(arr)):
    if arr[i] == "(":
        stk.append(arr[i])
    elif arr[i] == ")":
        stk.pop()
        if arr[i-1] == "(":
            answer += len(stk)
        else:
            answer += 1

print(answer)