n, m, k = map(int, input().split())

cnt = 0

while n>=2 and m>=1:
  n = n - 2
  m = m - 1
  if n+m < k:
    break
  cnt += 1

print(cnt)
