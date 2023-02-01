#10824 네수

voca = input()

arr = []
for i in range(len(voca)):
    arr.append(voca[i:])

arr.sort()
for i in range(len(arr)):
    print(arr[i])