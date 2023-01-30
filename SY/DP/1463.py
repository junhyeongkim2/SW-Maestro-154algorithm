n=int(input())
dp=[0]*(n+1)

for i in range(2,n+1):
	"""
	1빼기, 2나누기, 3나누기 중 횟수 연산 결과가 최대로 나옴
	10에서 1을 뺀 연산 예시
	dp[10]에서 1을 빼는게 아니라, dp[9]를 구하고 1 뺀 연산 횟수 1 더하기
	= dp[9]+1
	"""
	dp[i]=dp[i-1]+1

	"""
	4에서 2를 나눈 연산 예시
	11번째 줄 결과 -> dp[4]=dp[3]+1=2
	숫자가 커질수록 나누셈 결과 몫이 작기 때문에 나누기가 더 유리 -> 비교해보자
	dp[4]는 dp[2]를 구하고 2 나누기한 연산 횟수 1 더하기
	=dp[2]+1=2
	"""
	if(i%2==0):
		dp[i]=min(dp[i],dp[i//2]+1)

	"""
	9에서 3을 나눈 연산 예시
	11번째 줄 결과 -> dp[9]=dp[8]+1=4
	숫자가 커질수록 나눗셈 결과 몫이 작기 때문에 나누기가 더 유리 -> 비교해보자
	dp[9]는 dp[3]을 구하고 3 나누기한 연산 횟수 1 더하기
	=dp[3]+1=2
	"""
	if(i%3==0):
		dp[i]=min(dp[i],dp[i//3]+1)

print(dp[n])