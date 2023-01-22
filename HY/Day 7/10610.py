n = list(input())
#리스트를 내림차순하고 정수형으로 바꿈
n.sort(reverse=True)
n = list(map(int, n))
#30의 배수조건: 3의 배수(모든 자리 수의 합이 3의 배수) and  10의 배수여야함 (가장 작은 수가 0이어야함)
if sum(n) % 3 == 0 and  n[-1] == 0 :
  ##리스트를 다시 하나로 합치고 string으로 변환
  print(''.join(map(str, n )))
  #30의 배수가 아닐경우 -1
else :
  print(-1)

