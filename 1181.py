import sys

n=int(sys.stdin.readline())

lis=[]
for i in range(n):
    lis.append(sys.stdin.readline().strip())

lis=list(set(lis))
lis.sort()
lis.sort(key=len)

for i in lis:
    print(i)