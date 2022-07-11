import sys
input=sys.stdin.readline

T=int(input())

def resident(x,y):
    if x==0:
        return y
    elif y<=1:
        return 1
    return resident(x-1,y)+resident(x,y-1)

for i in range(T):
    k=int(input())
    n=int(input())
    print(resident(k,n))
