# 11004번 K번째 수
# https://www.acmicpc.net/problem/11004

# merge_sort를 직접 정의하여 구현
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = len(arr)//2 # 중앙값을 pivot으로 설정
    arr_left = merge_sort(arr[:pivot])
    arr_right = merge_sort(arr[pivot:])

    i, j, k = 0, 0, 0

    while i<len(arr_left) and j<len(arr_right):
        if arr_left[i] < arr_right[j]:
            arr[k]=arr_left[i]
            i+=1
        else:
            arr[k]=arr_right[j]
            j+=1
        k+=1

    if i==len(arr_left):
        while j<len(arr_right):
            arr[k]=arr_right[j]
            j+=1
            k+=1
    else:
        while i<len(arr_left):
            arr[k]=arr_left[i]
            i+=1
            k+=1

    return arr

_, K = map(int, input().split())
arr = list(map(int, input().split()))
print(merge_sort(arr)[K-1])