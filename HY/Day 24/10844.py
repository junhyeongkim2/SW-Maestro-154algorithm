import sys
input = sys.stdin.readline

n = int(input())
arr = [[0]* 10 for _ in range(n)]
for i in range(1,10):
    arr[0][i] = 1 #n=1 한자리인 경우
result = 0

#마지막 자리 엇갈려서 더하기 0번쨰 9번쨰는 따로 처리
for i in range(1, n) :
    #0번째는 이전것의 1번째값
    arr[i][0] = arr[i-1][1]
    arr[i][9] = arr[i-1][8]
    for j in range(1, 9) : #1부터 8 i번째 열, j번째의 것은 이전의 위아래의 합
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]

for i in range(10):
    result += arr[n-1][i]
print(result % 1000000000)