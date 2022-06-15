inp=map(int,input().split())
inp=list(inp)
slis=[]
for i in inp:
    slis.append(i**2)
print(sum(slis)%10)
