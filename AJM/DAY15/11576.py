A,B = map(int,input().split())
n = int(input())
arr = list(map(int,input().split()))
dec = 0
arr = arr[::-1]
for i in range(len(arr)):
    dec += arr[i]*A**i
answer = []
while(dec):
    answer.append(dec % B)
    dec //= B

print(*answer[::-1])