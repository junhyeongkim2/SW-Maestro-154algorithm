total = int(input())
for n in range(1, total+1):
    print(" "*(total-n) + "*" *n, end = '')
    print()