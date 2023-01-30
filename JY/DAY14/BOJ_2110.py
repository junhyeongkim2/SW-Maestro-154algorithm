import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input()))


house.sort()
start = 1
end = house[-1]-house[0]

res = 0
while start <= end:
    mid = (end+start) // 2 #최소 거리 mid라면
    count = 1
    before = house[0]
    for i in range(1, N):
        tmp = house[i] - before
        if tmp >= mid:
            count +=1
            before = house[i]

    if count >= C:
        start = mid + 1
        res = mid
    else:
        end = mid -1
print(res)
        
                
    
    