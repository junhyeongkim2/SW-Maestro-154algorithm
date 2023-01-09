import sys
input = sys.stdin.readline
N = int(input())
user = []
for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    user.append((age, name))
user.sort(key=lambda x:x[0])
for u in user:
    print(u[0], u[1])