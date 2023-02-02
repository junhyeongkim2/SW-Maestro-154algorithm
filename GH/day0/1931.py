n = int(input())
data = []
for i in range(n):
  data.append(list(map(int, input().split())))

data.sort(key=lambda x: (x[1], x[0]))

time = data[0][1]
cnt = 1

for i in data[1:]:
  if i[0]<time:
    continue
  else:
    cnt += 1
    time = i[1]

print(cnt)