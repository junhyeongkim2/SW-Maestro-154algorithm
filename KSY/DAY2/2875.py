n, m, k = map(int, input().split())
result = 0

while n >= 2 and m >= 1: #각 남녀가 팀을 이루면서 인원이 빠질 때 0이하가 되지 않을 때까지
    n -= 2
    m -= 1
    result += 1

mod = n + m
while mod < k: #제외할 인원이 팀을 이루지 못한 인원보다 많을 때
    result -= 1
    mod += 3

print(result)