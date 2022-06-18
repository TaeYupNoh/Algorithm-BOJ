a=[]
while True:
    a.append(list(map(int,input().split())))
    if [0, 0] in a:
        for i in range(len(a)-1):
             print(a[i][0]+a[i][1])
        quit()