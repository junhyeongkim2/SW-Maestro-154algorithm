n = input()
arr = []
#문자열 파싱
for i in range(len(n)):
  arr.append(n[i:])
arr.sort()
for i in arr :
    print(i)

