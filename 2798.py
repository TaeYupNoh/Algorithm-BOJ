from itertools import combinations

num,target=map(int,input().split())
lis=list(map(int,input().split()))
biggest=0

for i in combinations(lis,3):
    current=sum(i)
    if biggest < current <= target:
        biggest = current

print(biggest)