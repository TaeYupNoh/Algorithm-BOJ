n=int(input())

b=[]
for i in range(n):
    a=tuple(map(int,input().split()))
    b.append(a)

for j in b:
    r=1
    for compare in b:
        if j[0]<compare[0] and j[1]<compare[1]:
            r+=1
    print(r,end=" ")