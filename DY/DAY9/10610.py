# 10610번 30
# https://www.acmicpc.net/problem/10610

nums = list(input()) # str로 한 글자씩 저장
nums = list(map(int, nums)) # int로 변경

if sum(nums)%3: # 3의 배수가 아닐 시
    print(-1)
    exit()
else: # 3의 배수일 시
    ans = ''
    for num in sorted(nums, reverse=True):
        ans += str(num)

# 위에서 3의 배수인 것을 확인했으므로, 0만 있으면 30의 배수인 게 확인된 것임.
# 굳이 30의 배수인 걸 확인 안 해줘도 된다.
if not int(ans)%30:
    print(ans)
else:
    print(-1)