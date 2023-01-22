n, m, k = map(int, input().split())
result = 0 #총 팀수를 세는 변수
while n>=2 and m>=1 and n+m >= k+3 : #n이 2 이상, m이 1 이상, 남은 인원 수가 인턴인원 + 3 이상 일 때까지 진행
  n -= 2
  m -=1
  result += 1
print(result)