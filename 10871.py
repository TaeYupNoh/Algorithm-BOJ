a,b=map(int,input().split())
c=list(input().split())
d=[]
for i in range(len(c)):
    if int(c[i])<b:
        d.append(c[i])
print(' '.join(d))        