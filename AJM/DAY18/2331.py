# 반복 수열
import sys

input = sys.stdin.readline
A, P = map(int, input().split())

arr = [A]

while True:
    temp = 0
    for i in str(arr[-1]):
        temp += int(i) ** P
    if temp in arr:
        break
    else:
        arr.append(temp)

print(arr.index(temp))

# index함수는 temp가 arr에 몇번째에 처음 등장하는지를 알려줌
