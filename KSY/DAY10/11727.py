n = int(input())
tail = [-1]*(n+1)
tail[1:3] = [1, 3]

for i in range(3, n+1):
    tail[i] = tail[i-1] + tail[i-2]*2

print(tail[n] % 10007)
