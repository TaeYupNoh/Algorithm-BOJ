i=int(input())
a=[]
b=[]
while i>0:
    a.append(list(input().split()))
    i=i-1  
for i in range(len(a)):
    b.clear()
    for j in range(len(a[i][1])):
        b.append(a[i][1][j]*int(a[i][0]))
    print(''.join(b))        