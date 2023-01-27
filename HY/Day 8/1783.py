n, m = map(int, input().split())

result = 0
# n이 1일 때 무조건 1
if n == 1:
  result = 1
# n이 2일 때
elif n == 2: 
  if m >= 1 and m <= 6: #m이 1~6일 때
    result = (m + 1) // 2 
  elif m >= 7: #7이상일 때
    result = 4
# n이 3 이상일 때
elif n >= 3: 
  if m <= 6: #m이 1~6일 때
    result = min(m, 4)
  elif m >= 7: #m이 7 이상일 때
    result = m - 2
print(result)
