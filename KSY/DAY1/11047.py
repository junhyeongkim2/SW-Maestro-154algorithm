n, number = map(int, input().split())
alist = []
answer = 0

for _ in range(n):
    alist.append(int(input()))

#내 풀이 - 예제는 통과, 최종은 비통과
# n = alist[1]
#
# while True:
#     if number <= 0:
#         break
#     d, m = divmod(number, 10)
#     if m >= n:
#         answer += 1 + (m-n)
#         number //= 10
#     else:
#         answer += m
#         number //= 10
#

#참조 코드
for i in reversed(range(n)): #reversed 내장함수 **학습**
    answer += number//alist[i]
    number %= alist[i]

print(answer)
