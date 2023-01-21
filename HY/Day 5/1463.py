x = int(input())
d = [0] * (x + 1)

for i in range(2, x + 1):
  #1을 빼는 경우
  d[i] = d[i - 1] + 1
  #현재 수가 2로나눠지는 경우
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1)
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)
print(d[x])
