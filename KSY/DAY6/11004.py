
n, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
print(numbers[k-1])