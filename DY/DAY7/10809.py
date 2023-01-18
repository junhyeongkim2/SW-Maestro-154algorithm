pos = [-1]*26
count = 0
for i in input():
    if pos[ord(i)-97] == -1:
        pos[ord(i)-97] = count
    count += 1

for n in pos:
    print(n, end=' ')