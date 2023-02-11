# 내 풀이
# N = input()
# result = []
#
# while len(N) > 2:
#     byte3 = N[-3:]
#     N = N[:-3]
#     temp = 0
#     for i, n in enumerate(byte3):
#         temp += (2**(2-i))*int(n)
#     result.append(temp)
#
#     if len(N) < 3:
#         temp = 0
#         for i, n in enumerate(reversed(N)):
#             temp += (2 ** i) * int(n)
#         print(temp, end="")
#
# for i in reversed(result):
#     print(i, end="")


print(oct(int(input(), 2))[2:])
