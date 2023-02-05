import sys
input = sys.stdin.readline

N, K = map(int, input().split())
i = 0
alist = [i+1 for i in range(N)] #[1, 2, 3, 4, ...]
answer = []

for _ in range(N):
    i += K-1
    i %= len(alist)
    answer.append(alist[i])
    del alist[i]

print("<", end="")
for a in answer:
    if answer.index(a) == len(answer) - 1:
        print("%d>" % a)
        break
    print(a, end=", ")
