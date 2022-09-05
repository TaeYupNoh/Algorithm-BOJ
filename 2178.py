# 2178 미로 탐색
from collections import deque
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
trip = [[1 for _ in range(m)] for _ in range(n)]


def bfs(a, b):
    queue = deque([(a, b)])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()

        if x == n-1 and y == m-1:
            return trip[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '1' and visited[nx][ny] == False:
                queue.append((nx, ny))
                visited[nx][ny] = True
                trip[nx][ny] = trip[x][y] + 1


print(bfs(0, 0))
