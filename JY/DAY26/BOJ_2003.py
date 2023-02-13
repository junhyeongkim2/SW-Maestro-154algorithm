N, M = map(int, input().split())
A = list(map(int, input().split())) + [0]

right = 0
left = 0
res = A[0]
cnt = 0

while right < N:
    if res == M:
        right += 1
        res += A[right]
        res -= A[left]
        left += 1
        cnt += 1
        continue
    elif res < M:
        right +=1
        res += A[right]
        continue
    elif res > M:
        res -= A[left]
        left += 1
        continue
print(cnt)

