n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print("Case #"+ str(i+1) + ": " + str(a + b))