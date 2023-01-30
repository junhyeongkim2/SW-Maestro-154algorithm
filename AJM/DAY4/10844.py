#쉬운 계단 수

"""
나누기 잘 확인하기 !!!!

자리수가 2일때
맨뒤에 0이 올 수 있는 경우 1개(10)
맨뒤에 1이 올 수 있는 경우 1개(21)
맨뒤에 2가 올 수 있는 경우 12 32 2개

        0 1 2 3 4 5 6 7 8 9
한자리수 0 1 1 1 1 1 1 1 1 1
두자리수 1 1 2 2 2 2 2 2 2 1
세자리수 1 3 3 4 4 4 4 4 3 2

d[자리수][끝자리에 오는 수] = 양쪽 대각선의 합

끝자리가 0, j=0: d[i][j] = d[i-1][j+1]
끝자리가 1~8, j=1~8 : d[i][j] = d[i-1][j-1] + d[i-1][j+1]
끝자리가 9 ,j=9 : d[i][j] = d[i-1][j-1]
"""

n = int(input())
d = [[0]*10 for i in range(101)]

for i in range(1,10):
    d[1][i] = 1

for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i-1][j+1]
        elif j == 9:
            d[i][j] = d[i-1][j-1]
        else:
            d[i][j] = d[i-1][j-1]+d[i-1][j+1]
print(sum(d[n])%1000000000)