# 2444 별 찍기-7
n = int(input())
temp = n-1
for i in range(n):
    print(' '*temp + '*'*(2*i+1))
    temp -= 1
temp = 0
for j in range(n-1, 0, -1):
    temp += 1
    print(' '*temp + '*'*(2*j-1))
