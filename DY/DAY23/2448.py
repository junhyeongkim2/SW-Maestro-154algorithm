def draw_star(N):
    if N == 3:
        return ["*", "* *", "*****"]

    result = draw_star(N // 2)

    for i in range(N // 2):
        result.append(result[i] + ' ' * (len(result[(N // 2 - 1) - i])) + result[i])

    return result

if __name__ == '__main__':
    N = int(input())
    star = draw_star(N)
    for i in range(N):
        print(' ' * (N - i - 1) + star[i] + ' ' * (N - i - 1))