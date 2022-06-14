blis=[]
i=-1
while i==-1:
    inp=list(map(int,input().split()))
    blis.append(inp)
    if inp==[0,0]:
        i=0
for i in range(len(blis)):
    if blis[i][0] > blis[i][1]:
        print('Yes')
    elif blis[i][0] <= blis[i][1]:
        if blis[i][0] and blis[i][1] != 0:
            print('No')
