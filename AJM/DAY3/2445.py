#별 찍기 -8

n = int(input())

for i in range(1,n+1):
    print("*"*i+" "*(2*n-2*i)+"*"*i)
for i in range(1,n+1):
    print("*"*(n-i)+" "*(2*i)+"*"*(n-i))

