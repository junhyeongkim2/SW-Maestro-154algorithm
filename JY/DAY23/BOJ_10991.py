n=int(input())
total = n + (n-1)
for i in range(n):
    print(" " * ((total//2) -i) + "* " * (i+1))