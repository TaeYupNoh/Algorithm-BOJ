lis=[1,1,2,2,2,8]
inp=list(map(int,input().split()))
slis=[]
for i in range(6):
    slis.append(lis[i]-inp[i])
print(*slis)
