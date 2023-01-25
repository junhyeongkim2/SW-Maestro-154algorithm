n = int(input())

for i in reversed(range(n)):
    print(" "*i + (2*(n-i)-1)*"*")