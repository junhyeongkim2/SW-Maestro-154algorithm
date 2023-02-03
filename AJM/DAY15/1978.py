#1978 소수 찾기
n = int(input())

arr = list(map(int,input().split()))
cnt = 0
for p in arr:
    is_prime = 0
    if p == 1:
        continue
    else:
        for i in range(2,p+1):
            if p % i == 0:
                is_prime += 1
    if is_prime == 1:
        cnt += 1
print(cnt)
        