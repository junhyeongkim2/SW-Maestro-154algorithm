n = int(input())

for i in range(1, n+1):
    print("*"*i + 2*(n-i)*" " + "*"*i)

for i in reversed(range(1, n)):
    print("*"*i + 2*(n-i)*" " + "*"*i)
