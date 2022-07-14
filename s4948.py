# 4948 베르트랑 공준
n=[]
while 0 not in n:
    fir=int(input())
    n.append(fir)
    check = [True for i in range(2*fir+1)]
    for i in range(2, 2*fir+1):
        if check[i] == True:
            for j in range(i*2 , 2*fir+1, i):
                check[j] = False
            if fir < i <= 2*fir :
                print(i)
