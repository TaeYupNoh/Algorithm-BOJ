h,m=map(int,input().split())
tm=h*60+m-45
oh=tm//60
om=tm%60
if oh>=24:
    oh=0
if oh==-1:
    oh=23
print(oh,om)
