# ACM 호텔
t = int(input())
while t > 0 :
    h,w,n=map(int,input().split())
    a=n%h
    if a==0:
        b=n//h
        a=h
    else:
        b=n//h+1
    print(f'{a}{b:02d}')
    t-=1