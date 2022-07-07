# 15649 N과 M(2)
n,m=map(int,input().split())
lis = []

def dfs():
    if len(lis) == m:
        if lis == sorted(lis):
            print(*lis)
            return
        else :
            pass
    
    for i in range(1,n+1):
        if i in lis:
            continue
        lis.append(i)
        dfs()
        lis.pop()

dfs()