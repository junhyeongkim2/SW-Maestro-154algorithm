n=int(input())
card=list(map(int,input().split()))
card.sort()
m=int(input())
check=list(map(int,input().split()))
cnt={}
for i in card:
	if i in cnt:
		cnt[i]+=1
	else:
		cnt[i]=1

def binary(n):
	l=0
	r=len(card)-1

	while l<=r:
		mid=(l+r)//2

		if card[mid]==n:
			return cnt.get(n)
		elif card[mid]>=n:
			r=mid-1
		else:
			l=mid+1
	return 0

for i in check:
	print(binary(i),end=' ')
