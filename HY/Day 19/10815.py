"""
숫자 카드는 정수 하나가 적혀져 있는 카드이다.
상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때,
이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.
(1) set으로 풀기
순서와 중복에 대한 특성을 사용하지 않을때는 list보다는 set을 사용
import sys
input = sys.stdin.readline

n = int(input())
arr = set(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    if i in arr:
        print(1, end=" ")
    else:
        print(0, end=" ")
"""
""" 딕셔너리 사용
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
arr2 = list(map(int, input().split()))

dict = {}
for i in arr:
    dict[i] = 0

for j in arr2:
    if j in dict:
        print(1, end=' ')
    else:
        print(0, end=' ')
        """

"""이진탐색 사용"""
import sys
input = sys.stdin.readline

# 가지고 있는 카드
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# 임의의 카드
m = int(input())
arr2 = list(map(int, input().split()))

start, end = 0, n
check = False
while start <= end:
    for i in arr2:
        mid = (start + end) // 2
        if arr[mid] > i:  # 중간 값보다 작다면
            end = mid - 1  # 중간보다 왼쪽 한 칸 옆까지 탐색
        elif arr[mid] < i:  # 중간 값보다 크다면
            start = mid + 1  # 중간보다 오른쪽 한 칸 옆부터 탐색
        else:
            check = True
            break
    if check == True:
        print(1, end=" ")
    else:
        print(0, end=" ")
