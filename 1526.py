# 1526 가장 큰 금민수
n = int(input())
for i in range(n,0,-1):
    for check in str(i):
        if check in '01235689':
            break
    else:
        print(i)
        break