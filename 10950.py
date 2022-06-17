a=int(input())
b=[]
for i in range(a):
    b.append(list(map(int,input().split())))
for j in range(len(b)):
    print(b[j][0]+b[j][1])
