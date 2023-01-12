import sys
input = sys.stdin.readline

n,k = map(int, input().split())
box = list(map(int, input().split()))
box.sort()
print(box[k-1])