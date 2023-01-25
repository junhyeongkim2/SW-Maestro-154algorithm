n = int(input())

for i in reversed(range(1, n+1)):
    print(" "*(n-i) + "*"*(2*i-1))

for i in range(2, n+1):
    print(" "*(n-i) + "*"*(2*i-1))