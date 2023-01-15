def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

M, N = map(int, input().split())

for n in range(M, N+1):
    if isPrime(n):
        print(n)