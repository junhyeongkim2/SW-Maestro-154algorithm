import sys
import math

input = sys.stdin.readline

A, B = map(int, input().split())
total = int(input())
numbers = list(map(int, input().split()))

res = 0
cnt = total

ans = []
for i in range(total):
    res = res + numbers[i]* (A**(cnt -1))
    cnt -= 1

while res > 0:
    ans.append(str(res%B))
    res = res//B
ans = ans[::-1]
print(" ".join(ans))

            
        
        
    
        