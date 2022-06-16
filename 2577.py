i=3
a=[]
while i>0:
    a.append(int(input()))
    i=i-1
b=str(a[0]*a[1]*a[2])
for k in range(10):
    c=0
    for j in range(len(b)):
        if int(b[j])==k:
            c=c+1
    print(c)
