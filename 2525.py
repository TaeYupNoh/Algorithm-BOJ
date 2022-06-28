# 오븐 시계
h,m = map(int,input().split())
pls = int(input())

if m+pls >=60:
    h=h+(m+pls)//60
    m=m+pls-(m+pls)//60*60
else:
    m=m+pls
if h>=24:
    h-=24
print(h,m)
