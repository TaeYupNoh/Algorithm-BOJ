#좌표 정렬하기
import sys
n=int(sys.stdin.readline())

lis=[]
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    lis.append((x,y))

lis.sort(key=lambda x:x[1])
lis.sort(key=lambda x:x[0])

[print(i[0],i[1]) for i in lis]