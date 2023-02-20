"""
반복수열
"""
import sys
input = sys.stdin.readline

#a: 수열의 시작 p: 몇제곱할지
a, p = map(int, input().split())
arr=[a]

while True:
    sum = 0 
    stra =list(str(a)) #a를 str로 변환하여 각 자리를 list로 만들어줌
    for i in stra: #수를 곱해주고 배열에 넣어줌
        sum += int(i) ** p
    if sum in arr: #이미 배열에 있다면
        start = arr.index(sum) #해당 값의 인덱스를 찾아서 strat부터 끝까지 삭제
        del arr[start:]
        break
    else: #배열에 없다면 추가하고, a로 설정
        arr.append(sum)  
        a = arr[-1]  

print(len(arr))

    