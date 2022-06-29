# 평균은 넘겠지
t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    sum=-a[0]
    for j in a:
        sum+=j
    avg=sum/a[0]
    cnt=0
    for k in a[1:]:
        if k>avg:
            cnt+=1
    print(f'{cnt/a[0]*100:.3f}%')
