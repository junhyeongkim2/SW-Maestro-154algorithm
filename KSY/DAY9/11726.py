n = int(input())
tail = [-1]*(n+1)
tail[1:3] = [1, 2]

for i in range(3, n+1):
    tail[i] = tail[i-2] + tail[i-1]

print(tail[n] % 10007) #10007로 나눈 나머지(문제 요구사항 잘 파악하기)
