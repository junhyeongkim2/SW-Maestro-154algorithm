s = input()

data = []
# 0이 등장하는가
zero = False
# 각 자리수를 더한것
sum = 0

for i in s:
    n = int(i)
    
    sum += n
    if n == 0:
        zero = True
    data.append(i)
    
if not zero or sum%3!=0:
    print(-1)
else:
    data.sort(reverse=True)
    print("".join(data))