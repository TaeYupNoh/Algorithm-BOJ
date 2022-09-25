# N과 M(8)


n,m = map(int,input().split())
lis = sorted(list(map(int,input().split())))
making = []


def dfs(depth):
    if len(making) == m:
        print(' '.join(map(str,making)))
        return
    for i in range(n):
        if len(making) == 0 or making[depth - 1] <= lis[i]:
            making.append(lis[i])
            dfs(depth +1)
            making.pop()


dfs(0)

