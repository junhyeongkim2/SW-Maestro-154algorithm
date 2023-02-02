import sys
input = sys.stdin.readline

target = int(input())
countButton = int(input())
brokenButton = list(input().split())

min_move = abs(target - 100)  # +/-로만 이동한 횟수

for number in range(1000001):
    number = str(number)

    for i, n in enumerate(number):
        if n in brokenButton:  # 고장난 버튼이 존재 하는 number, 더 볼 것도 없이 다음 수...
            break
        if i == len(number) - 1:  # 고장난 버튼 없이 이동할 수 있는 숫자
            min_move = min(min_move, abs(target - int(number)) + len(number))

print(min_move)
