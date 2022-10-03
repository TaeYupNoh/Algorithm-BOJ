# 10026 적록색약
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
color = [input() for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs(a,b,visit,graph):
    if visit[a][b] == 1:
        return 0
    else:
        start = graph[a][b]
        visit[a][b] = 1
        queue = deque([(a,b)]) 
        while queue:
            x,y = queue.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx < n and 0<= ny < n and visit[nx][ny] == 0 and graph[nx][ny] == start:
                    queue.append((nx,ny))
                    visit[nx][ny] = 1
        return 1


# 정상
nor_visited = [[0 for _ in range(n)] for _ in range(n)]

cnt_1 = 0
for i in range(n):
    for j in range(n):
        cnt_1 += bfs(i,j,nor_visited,color)

# 색약
nongreen_visited = [[0 for _ in range(n)] for _ in range(n)]
nongreen_color = color[:]

for i in range(n):
    if 'G' in nongreen_color[i]:
        nongreen_color[i] = nongreen_color[i].replace('G','R')

cnt_2 = 0
for i in range(n):
    for j in range(n):
        cnt_2 += bfs(i,j,nongreen_visited,nongreen_color)

print(cnt_1,cnt_2)