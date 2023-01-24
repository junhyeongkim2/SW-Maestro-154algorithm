#스티커

"""
(0,0) (0,1) (0,2) (0,3) (0,4)
(1,0) (1,1) (1,2) (1,3) (1,4)

50 10 100 20 40
30 50 70  10 60

규칙

카드의 크기가 2일때의 최대값은 그냥 대각선 더한거
2이상일때는 첫번째 줄이면 두번째줄의 두칸 전 or 한칸 전 중에 큰거 + 현재 카드 값
두번째 줄이면 첫번째줄의 "" 

"""
n = int(input())

for i in range(n):
    x = int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]

    #카드가 2장일때
    if x>1:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]

    for i in range(2,x):
        arr[0][i] += max(arr[1][i-2],arr[1][i-1])
        arr[1][i] += max(arr[0][i-2],arr[0][i-1])

    print(max(arr[0][x-1],arr[1][x-1]))
