import sys

input = sys.stdin.readline
N = int(input())
def fac(num):
    if num == 0:
        return 1
    return num* fac(num-1)
res = list(str(fac(N)))
res = res[::-1]
ans = 0
for i in range(len(res)):
    if res[i] == "0":
        ans += 1
    else:
        print(ans)
        break
