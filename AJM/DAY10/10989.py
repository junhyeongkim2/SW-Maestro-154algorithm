#10989 수 정렬하기 3
#for 문 안에서 append하면 메모리 재할당이 이루어져서 효율적으로 사용할 수 없다.
#모든 입력을 배열에 저장하면 메모리가 초과됨.

"""
계수 정렬(Counting Sort) 알고리즘
: 배열의 인덱스를 특정한 데이터의 값으로 여기는 정렬 방법
배열의 크기는 데이터의 범위를 포함할 수 있도록 설정.
데이터가 등장한 횟수를 셈. 
"""
import sys

n = int(sys.stdin.readline())
arr = [0]*10001

for i in range(n):
    data = int(sys.stdin.readline().strip())
    arr[data] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)