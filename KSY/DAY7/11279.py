import sys
import heapq
input = sys.stdin.readline

n = int(input())
numbers = []
heapq.heapify(numbers)

for _ in range(n):
    number = int(input())
    if number == 0:
        if len(numbers) == 0:
            print(0)
        else:
            print(heapq.heappop(numbers)[1])
    else:
        heapq.heappush(numbers, (-number, number))

