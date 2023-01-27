n = input()
n = [str(i) for i in n]
n.sort(reverse=True)

result = int(''.join(n))

if result % 30 != 0:
    print(-1)
else:
    print(result)
