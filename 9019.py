# 9019 DSLR
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())


def dslr(cmd: str,x: int):
    if cmd == 'D':
        return 2*x%10000
    elif cmd == 'S':
        return 9999 if x==0 else x-1
    elif cmd == 'L':
        front = x % 1000
        back = x // 1000
        return front*10 + back
    else:
        front = x % 10
        back = x // 10
        return front*1000 + back 


def bfs(start, end):
    queue = deque([('',start)])
    visited = set()
    visited.add(start)
    d = ['D','S','L','R']

    while queue:
        cmd, x = queue.popleft()
        if x == end:
            print(cmd)
            break
        for i in range(4):
            answer = dslr(d[i], x)
            if answer not in visited:
                visited.add(answer)
                queue.append((cmd+d[i],answer))


for _ in range(t):
    a,b = map(int,input().split())
    bfs(a,b)