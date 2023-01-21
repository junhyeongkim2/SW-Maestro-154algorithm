N = int(input())
times = list(map(int, input().split(' ')))
times.sort(reverse=True)

result = 0 # 시간 더 짧음
for i in range(1, N+1):
    result += i * times[i-1]
print(result)

"""
sum_time = 0
for i in range(N, 0, -1):
    min_time = min(times)
    sum_time += min_time * i
    times.remove(min_time)
print (sum_time)
"""