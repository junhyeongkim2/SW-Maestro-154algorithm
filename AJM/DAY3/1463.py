#1로 만들기

"""
DP
n = 3일 경우
d[1] = 0
d[2] = d[2] = d[1]+1 = 1
d[2] = min(d[2],d[1]+1) = 1
d[3] = d[2]+1
d[3] = min(d[3],d[3//3]+1) = 1

n = 4일 경우
d[4] = d[3] + 1 = 2
d[4//2]+1 = d[2] = 2
"""

n = int(input())

d = [0]*(n+1)

for i in range(2,n+1): 
    d[i] = d[i-1]+1
    if i%2 == 0:
        d[i] = min(d[i],d[i//2]+1)
    if i%3 == 0:
        d[i] = min(d[i],d[i//3]+1)
print(d[n])
    
