# 1158번 요세푸스 문제
# https://www.acmicpc.net/problem/1158

# deque을 쓰는 것보다 list를 쓰는 것이 더 빠름.
# join을 이용해 print 하는 방법 알아두기

N, K = map(int, input().split())
nums = [i for i in range(1, N+1)]

pos = 0
ans = []
while nums: # que가 빌 때까지 반복
    pos = (pos+(K-1))%len(nums)
    ans.append(nums.pop(pos))

print(f"<{', '.join(map(str, ans))}>")