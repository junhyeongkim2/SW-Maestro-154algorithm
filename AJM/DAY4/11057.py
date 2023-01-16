"""
나누기 잘 확인하기 !!!!

끝자리 수 0 1 2 3 4 5 6 7 8 9

한자리 수 1 1 1 1 1 1 1 1 1 1
두자리 수 1 2 3 4 5 6 7 8 9 10
세자리 수 1 3 6 10 15 21

d[i][j] = d[i-1][0~j까지]의 합
"""

n = int(input())
d = [[0]*10 for i in range (1001)]

for i in range(10):
    d[1][i] = 1
    
for i in range(2,n+1):
    for j in range(10):
        d[i][j] = sum(d[i-1][0:j+1])
            
print(sum(d[n])%10007)
