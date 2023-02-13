import sys
read = sys.stdin.readline

N = read()
cards = list(map(int, read().split()))

M = sys.stdin.readline()
candidate = list(map(int, read().split()))

cnt = {}
for i in cards:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in candidate:
    if cnt.get(i) != None:
        print(cnt.get(i), end=' ')
    else:
        print(0, end=' ')