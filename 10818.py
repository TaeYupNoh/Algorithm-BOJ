a=int(input())
b=list(map(int,input().split()))
c=-1000000
d=1000000
for i in range(len(b)):
        if b[i]>=c:
            c=b[i]
        if b[i]<=d:
            d=b[i]
print(d,c)
