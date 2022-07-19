# 15649 N과 M(1)
n,m=map(int,input().split())
lis=[]

def dfs():
    if len(lis)==m:
        print(*lis)
        return

    for i in range(1,n+1):
        if i in lis:
            # 이번 반복 안의 모든 내용을 넘어가고 다음 반복으로 보냄
            continue
        lis.append(i)
        dfs()
        lis.pop()

dfs()

# from itertools import permutations 를 활용한 풀이

from itertools import permutations

n,m=map(int,input().split())
lis=[i for i in range(1,n+1)]
all = permutations(lis,m)

for i in list(all):
    print(*i)
