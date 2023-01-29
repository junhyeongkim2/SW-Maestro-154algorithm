#11652 카드
import sys
n = int(input())

dic = {}

for i in range(n):
    num = int(sys.stdin.readline())
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
answer = sorted(dic.items(), key=lambda x :(-x[1],x[0]))

print(answer[0][0])