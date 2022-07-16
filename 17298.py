# 17928 오큰수
import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int, input().split()))
res = [-1]*n
stack = []

for i in range(n):
    while stack and lis[stack[-1]] < lis[i]:
        res[stack.pop()] = lis[i]
    stack.append(i)

print(*res)
