#제곱수의 합

"""

틀린 코드 그리디라고 생각함. 예외 50 
무조건 큰 제곱수 순으로 나타내면 가장 적게 더하는 거라고 생각함. 

import math

n = int(input())
result = 0
m = math.floor(n**0.5)

while(n>0):
    n -= m**2
    while( m**2 > n):
        m -= 1
    result += 1

print(result)
    
"""

n = int(input())

dp = [i for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j] + 1 : #n에서 제곱수 뺸 수의 최솟값 + 1
            dp[i] = dp[i-j*j] + 1 
print(dp[n])
        
