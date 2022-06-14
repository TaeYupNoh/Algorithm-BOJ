a=int(input())
b=[]
while a >0:
    b.append(input())
    a=a-1
for i in range(len(b)):
    c=len(b[i])
    try:
        print(b[i][0],b[i][c-1],sep='')
    except:
        print(b[i][0],b[i][0],sep='')
