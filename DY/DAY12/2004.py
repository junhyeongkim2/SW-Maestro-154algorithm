# 2004번 조합 0의 개수
# https://www.acmicpc.net/problem/2004

# dp를 쓰면 메모리 초과
# 기존 factorial을 쓰면 시간 초과
# 위 방법을 쓰지 않고 0의 개수를 찾아야 함.
# n!에서 k의 인수 개수 찾는 법?
# k로 계속 나누면서(안 나눠질 때까지) 몫을 더하면 그게 인수 개수임.

N, K = map(int, input().split())

def factor(n, k): # n!의 k 인수의 개수 구하기
    cnt = 0
    while n:
        cnt += n // k
        n //= k
    return cnt

remd_two = factor(N,2)-factor(N-K,2)-factor(K,2)
remd_five = factor(N,5)-factor(N-K,5)-factor(K,5)

print(min(remd_five,remd_two))