import sys
input = sys.stdin.readline

total = int(input())

room = []

for _ in range(total):
    s, e = map(int, input().split())
    room.append([s, e])

room.sort(key = lambda x : (x[1], x[0]))

count = 1
end = room[0][1]
for k in range(1, len(room)):
    if room[k][0] >= end:
        count +=1
        end = room[k][1]

print(count)