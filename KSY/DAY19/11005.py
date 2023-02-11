N, B = map(int, input().split())
result = []
days = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

while N > 0:
    result.append(N % B)
    N //= B
for i in reversed(result):
    if i > 9:
        print(days[i-10], end="")
    else:
        print(i, end="")
