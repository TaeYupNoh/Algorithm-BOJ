n = int(input())
queen = [0]*n
cnt = 0


def dfs(n, queen, col):
    global cnt
    if col == n:
        cnt += 1
        return

    for i in range(n):
        queen[col] = i

        for j in range(col):
            if queen[col] == queen[j]:
                break
            if abs(queen[col]-queen[j]) == (col - j):
                break

        else:
            dfs(n, queen, col+1)


dfs(n, queen, 0)
print(cnt)
