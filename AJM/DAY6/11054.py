#가장 긴 바이토닉 부분 수열

n = int(input())

arr = list(map(int,input().split()))
reverse_arr = arr[::-1]

dp1 = [1]*n
dp2 = [1]*n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]: #커질 때만
            dp1[i] = max(dp1[i],dp1[j]+1)
            
        if reverse_arr[i] > reverse_arr[j]: #작을 때만
            dp2[i] = max(dp2[i],dp2[j]+1)

dp2 = dp2[::-1]

answer = [0]*n

for i in range(n):
    answer[i] = dp1[i]+dp2[i]-1

print(max(answer))
            
