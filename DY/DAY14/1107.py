# 1107번 리모컨
# https://www.acmicpc.net/problem/1107

channel = int(input())
but = []
if int(input()): # 0이 아닌 경우에만 입력받음
    but = list(map(int,input().split()))

cnt = abs(100-channel) # +, -로만 이동하는 경우
for i in range(1000001):
    num = str(i)

    for n in range(len(num)):
        if int(num[n]) in but: # 고장난 버튼을 눌러야 하는 경우
            break

        if n==len(num)-1: # 끝까지 도달한 경우
            cnt = min(cnt, len(num)+abs(int(num)-channel))
print(cnt)