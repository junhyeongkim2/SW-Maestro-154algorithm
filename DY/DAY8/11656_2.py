# 11656번 접미사 배열
# https://www.acmicpc.net/problem/11656

# merge_sort를 직접 구현하여 풀이
def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i,j,k = 0,0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else: # right 값이 더 작은 경우
            arr[k]=right[j]
            j+=1
        k+=1

    if i==len(left):
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    else: # right 값이 다 들어간 경우
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
    return arr

word = input()
result = []
for i in range(len(word)):
    result.append(word[i:])

for ans in merge_sort(result):
    print(ans)