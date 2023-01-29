import sys

input = sys.stdin.readline

N = int(input())
correct = list(map(int, input().split()))
#sorted(correct) #-> 틀림 새로 생성되는 것임 
correct.sort()

M = int(input())
ch = list(map(int, input().split()))



def search(k):
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) //2
        if correct[mid]  == k:
            return 1
        elif correct[mid] > k:
            end = mid - 1
        else:
            start = mid+1
            
    return 0

for num in ch:
    print(search(num), end = " ")
