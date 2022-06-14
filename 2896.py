a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=100
d=[]
for i in range(3):
    if a[i]/b[i]<c :
        c = a[i]/b[i]
for j in range(3):
    d.append(a[j]-b[j]*c)

print(*d)
