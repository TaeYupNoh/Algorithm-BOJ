# 1094 막대기
x = int(input())

cnt=0
for temp in bin(x):
    if temp == '1':
        cnt +=1

print(cnt)