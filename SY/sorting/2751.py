import sys
# n의 범위가 1<=n<=1,000,000 이므로 시간초과 -> sys.stdin.readline() 사용
n=int(sys.stdin.readline())
li=[int(sys.stdin.readline()) for _ in range(n)]
li.sort()

for i in li:
	print(i)