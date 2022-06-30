# 한수
N=int(input())

def hansu(n):
    cnt=0
    for i in range(1,n+1):
        num_lis=list(map(int,str(i)))
        if i < 100:
            cnt+=1
        elif num_lis[0]-num_lis[1] == num_lis[1]-num_lis[2] :
            cnt+=1
    return cnt

print(hansu(N))