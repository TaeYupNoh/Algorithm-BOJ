a=[]
i=9
b=0
c=-1
while i>0:
    a.append(int(input()))
    i=i-1
for i in range(9):
    if a[i]>b:
        b=a[i]
        c=i+1
print(b)
print(c)
