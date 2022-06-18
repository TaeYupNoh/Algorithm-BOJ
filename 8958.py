a=int(input())
b=[]
c={}
while a>0:
    b.append(input())
    a=a-1
for i in range(len(b)):
    s=0
    ss=0
    for j in range(len(b[i])):
        if b[i][j]=='O':
            s=s+1
            ss=ss+s
        else:
            s=0
    print(ss)
