i=int(input())

a=[] # x,y 튜플 리스트
for j in range(i):
    a.append(tuple(map(int,input().split())))

a=sorted(a,key=lambda x:x[0])
a=sorted(a,key=lambda y:y[1])

for k in range(i):
    print(*a[k])