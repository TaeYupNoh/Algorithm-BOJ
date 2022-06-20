a=list(map(int,input().split()))
x,y=a[0],a[1]
w,h=a[2],a[3]
m=min(x-0,w-x,y-0,h-y)
print(m)