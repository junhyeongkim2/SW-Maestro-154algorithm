n = int(input())
for i in range(1, n+1):
    print("*" * i + " "*(2*n-i*2) + "*" * i)
for i in range(1, n+1):
    print("*"*(n-i) + " "*(i*2)+"*"*(n-i))
