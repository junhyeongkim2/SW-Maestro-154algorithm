n=int(input())
cnt=0

def hanoi(n,start,tmp,end):
	if n==1:
		print(start,end)
		return
	else:
		hanoi(n-1,start,end,tmp)
		print(start,end)
		hanoi(n-1,tmp,start,end)
print(2**n-1)
hanoi(n,1,2,3)