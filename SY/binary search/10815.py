n=int(input())
card=list(map(int,input().split()))
card.sort()
m=int(input())
check=list(map(int,input().split()))

def binary(m):
	l=0
	r=len(card)-1

	while l<=r:
		mid=(l+r)//2

		if card[mid]==m:
			return 1
		elif card[mid]>=m:
			r=mid-1
		else:
			l=mid+1
	return 0

for i in check:
	print(binary(i),end=' ')