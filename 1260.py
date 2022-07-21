# DFS와 BFS
from collections import deque

n,m,start=map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    graph[i].sort()

def dfs(x):
    visited[x]=True
    print(x,end=' ')
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

def bfs(x):
    queue=deque([x])
    visited[x]=True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]= True

visited = [False]*len(range(n+1))
dfs(start)
print()
visited = [False]*len(range(n+1))
bfs(start)
