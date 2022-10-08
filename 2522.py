# 2522 별 찍기-12
n = int(input())

for a in range(1,n+1):
    print(' '*(n-a) + '*'*(a))

for a in range(1, n):
    print(' '*a + '*'*(n-a))