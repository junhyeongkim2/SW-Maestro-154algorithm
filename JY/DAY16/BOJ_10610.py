import sys

input = sys.stdin.readline

tmp = list(input().rstrip())
tmp.sort(reverse=True)

sum = 0
if "0" not in tmp:
    print(-1)
else:
    for i in tmp:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        print("".join(tmp))
        
    
    
