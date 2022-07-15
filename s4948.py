# 4948 베르트랑 공준
n=[]
while True:
    fir=int(input())
    if fir == 0:
        break
    n.append(fir)
    check = [True for i in range(2*fir+1)]
    cnt=0
    for i in range(2, 2*fir+1):
        if check[i] == True:
            for j in range(i*2 , 2*fir+1, i):
                check[j] = False
            if fir < i <= 2*fir :
                cnt+=1
    print(cnt)
