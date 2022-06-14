a=int(input())
b=list(map(int,input().split()))
c=0
d=[]
e=0
for i in range(len(b)):
    if b[i]>=c:
        c=b[i]
for i in range(len(b)):
    d.append(float(b[i]/c*100))
for i in range(len(d)):
    e=e+d[i]
print(e/len(d))
