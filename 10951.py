lis=[]
while True:
    try :
        a,b=map(int,input().split())
        c=a+b
        lis.append(c)
    except :
        for i in range(len(lis)):
            print(lis[i])
        quit()
