n = int(input())
a = 1
for i in range(1, n+1):
    if i == n:
        print("*"*(2*n - 1))
    else:
        if i == 1:
            print(" " * (n - i) + "*")
        else:
            print(" "*(n-i) + "*" + " "*a + "*")
            a += 2
