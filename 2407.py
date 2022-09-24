# 2407 조합

n, m= map(int,input().split())
if n//2 <m:
    m = n-m

up = 1
for i in range(n,n-m,-1):
    up *= i

down = 1
for i in range(1,m+1):
    down *= i

print(up//down)