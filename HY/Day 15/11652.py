
import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for i in range(n):
  card = int(input())
  if card in dic:
    dic[card] +=1 # { 4:1, 5:2, 2:3 } 이런식으로 딕셔너리에 몇개 들어갔는지가 입력됨
  else:
    dic[card] = 1

#dic.items(): 변수에 튜플로 이루어진 리스트를 담는다
# ex) result [(4,1), (5,2), (2,3)] 람다식을 이용하여 갯수를 먼저 내림차순하고, 
# card을 오름차순하여 갯수가 같으면 작은 수가 출력될 수 있게 정렬한다
#람다식은 먼저 쓴 것을 우선순위로 정렬함, 1번째 인덱스(카드갯수)를 내림차순 하고, 0번째 인덱스를 오름차순
result = sorted(dic.items(), key = lambda x:(-x[1],x[0]))

#result의 첫번째 튜플 인덱싱(1개만 추출)
print(result[0][0])
