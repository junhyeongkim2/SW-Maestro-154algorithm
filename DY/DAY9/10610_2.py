# 10610번 30
# https://www.acmicpc.net/problem/10610

nums = list(input()) # str로 한 글자씩 저장
nums.sort(reverse=True)

if nums[-1]=='0' and sum(list(map(int, nums)))%3==0:
    print(''.join(nums))
else:
    print('-1')

