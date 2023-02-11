days = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


N, B = input().split()
result = 0

for i, n in enumerate(reversed(N)):
    if n in days:
        result += (days.index(n)+10) * (int(B) ** i)
    else:
        result += int(n) * int(B) ** i

print(result)
