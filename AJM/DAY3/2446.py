#별 찍기 -9

n = int(input())

for i in range(n):
    print(" "*i+"*"*(2*n-2*i-1))
for i in range(1,n):
    print(" "*(n-i-1)+"*"*(2*i+1))
