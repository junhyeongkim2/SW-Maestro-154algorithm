#별 찍기 -17

n = int(input())

for i in range(1,n):
    if i ==1:
        print(" "*(n-i)+"*")
    else:
        print(" "*(n-i)+"*"+" "*(2*(i-1)-1)+"*")
print("*"*(2*(n-1)+1))
