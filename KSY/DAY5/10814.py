n = int(input())
peopleList = []

for i in range(n):
    age, name = input().split()
    peopleList.append((int(age), name))

peopleList.sort(key=lambda x: x[0])

for a, n in peopleList:
    print(a, n)