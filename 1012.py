# 1012 유기농 배추
# dfs 활용 풀이
from collections import deque
import sys
# 재귀 limit 기본이 10**3이고 이 풀이는 10**4 필요
sys.setrecursionlimit(10**4)


def dfs(a, b):
    if a < 0 or a >= n or b < 0 or b >= m:
        return
    if visited[a][b] == False and graph[a][b] == 1:
        visited[a][b] = True
        dfs(a+1, b)
        dfs(a-1, b)
        dfs(a, b+1)
        dfs(a, b-1)
        return 1
    return 0


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0
    queue = deque()
    for i in range(n):
        for j in range(m):
            cnt += dfs(i, j)
    print(cnt)
