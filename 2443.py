# 2443 별 찍기-6
n = int(input())
for i in range(n):
    star = 2*n-(2*i+1)
    print(' ' * i + '*' * star)
