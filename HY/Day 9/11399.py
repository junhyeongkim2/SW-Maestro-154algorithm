n = int(input())
p = list(map(int, input().split()))
p.sort(reverse=False)
arr = []
result = 0
for i in range(0,n):
  result = p[i] + result
  arr.append(result)
print(sum(arr))