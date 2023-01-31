import sys

input=sys.stdin.readline
total, N = map(int, input().split())
num= []

for i in range(total):
    num.append(int(input()))

start = 1
end = max(num)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(total):
        cnt += num[i] // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
