
#2745 진법 변환
answer = 0

N,B = map(str,input().split())
B = int(B)

N = N[::-1]
answer = 0

for i,n in enumerate(N):
    if n.isdigit():
        answer += int(n)*B**i
    else:
        answer += (ord(n)-55)*B**i

print(answer)