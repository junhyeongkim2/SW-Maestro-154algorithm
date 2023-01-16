n=int(input())
li=[int(input()) for _ in range(n)]
dp=[0]*n
dp[0]=li[0]
if n>1:
	dp[1]=li[0]+li[1]
if n>2:
	"""
	마지막 계단은 무조건 밟아야 함
	따라서,
		x o x -> 이 경우는 성립하지 않으므로 비교하지 않음
		o x o
		x o o
	다음과 같은 조건 중 최대 점수인 조건으로 계단을 오른다
	"""
	dp[2]=max(li[0]+li[2],li[1]+li[2])

for i in range(3,n):
	"""
	마지막 계단은 무조건 밟아야 함 -> for문으로 검사할 때 마지막은 밟도록 함
	연속 3개를 오를 수 없음 -> 경우의 수는 o o x o / o x o o 임
	따라서,
		 dp영역 x o
		dp영역 x o o
	다음과 같은 조건 중 최대 점수인 조건으로 계단을 오른다

	"""
	dp[i]=max(dp[i-3]+li[i-1]+li[i], dp[i-2]+li[i])

print(dp[n-1]) #dp의 최대값이 아니라 계단을 오른 최종 점수를 출력