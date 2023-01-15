import sys
def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False
    return True

N = map(int, sys.stdin.readline())
num = list(map(int ,sys.stdin.readline().split()))
count = 0
for i in num:
    if isPrime(i) == True:
        count += 1
print(count)