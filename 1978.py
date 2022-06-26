import sys

n=int(sys.stdin.readline())
lis=list(map(int,sys.stdin.readline().split()))

if 1 in lis:
    lis.remove(1)

num_prime=0
for i in lis:
    cnt=0

    for j in range(2,i+1): 
        if i%j == 0:
            cnt+=1

    if cnt == 1:
        num_prime+=1

print(num_prime)
            