n, k = map(int, input().split())
coins = []
for j in range(n):
  coins.append(int(input()))
#큰 수부터 오름차순
coins.sort(reverse=True)
result = 0

for i in coins:
  #각각의 동전(i)을 확인하며, 가장 큰 돈으로 먼저 나누고,  다음 i로 넘어감 n에는 나눠진 후 남은 돈만큼 들어감
  #예를 들어, 1500원을 나누면, 1000원으로 나누고, result는 나눠진 횟수(나눈 몫)을 더한다, 나눈 후 나머지는 n이 되고 그다음 500원으로 나눈다.
  result += k // i
  k = k % i
  #1460원을 1000원으로 1번 나누고, 100원으로 4번 50원으로 1번 10원으로 1번 나눠진다 result는 따라서 총 7이 나온다
#result는 총 필요한 동전의 갯수 = 위에서 진행된 횟수가 임력됨
print(result)