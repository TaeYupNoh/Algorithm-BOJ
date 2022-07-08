# N과 M(3)
n,m=map(int,input().split())
lis=[]

def backtracking():
    if len(lis)==m:
        print(*lis)
        return

    for i in range(1,n+1):
        lis.append(i)
        backtracking()
        lis.pop()

backtracking()
