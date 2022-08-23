# 1012 유기농 배추
# BFS 풀이
from collections import deque
import sys
input = sys.stdin.readline


def bfs(a, b):
    queue = deque([(a, b)])
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
                queue.append((ny, nx))
                graph[ny][nx] = 2

    return 1


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += bfs(i, j)

    print(cnt)
