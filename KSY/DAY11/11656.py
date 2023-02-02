S = input()
strings = []

for i in range(len(S)):
    strings.append(S[i:])

strings.sort()
for s in strings:
    print(s)