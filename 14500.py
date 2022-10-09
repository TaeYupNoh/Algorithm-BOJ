# 14500 테트로미노
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0
max_val = max(map(max, graph))


def backTracking(x, y, temp, depth):
    global answer
    if temp + max_val*(3-depth) <= answer:
        return

    if depth == 3:
        answer = max(answer, temp)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                continue

            if depth == 1:
                visited[nx][ny] = True
                backTracking(x, y, temp + graph[nx][ny], depth + 1)
                visited[nx][ny] = False

            visited[nx][ny] = True
            backTracking(nx, ny, temp + graph[nx][ny], depth + 1)
            visited[nx][ny] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        backTracking(i, j, graph[i][j], 0)
        visited[i][j] = False

print(answer)
