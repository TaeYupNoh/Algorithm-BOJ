# 6606 로또
k = []
lis = []
while True:
    temp = []
    temp += map(int, input().split())
    if temp[0] == 0:
        break
    k.append(temp[0])
    lis.append(temp[1:])

temp = []


def back_tracking(x, i):
    if x == 6:
        print(*temp)

    for j in range(len(lis[i])):
        if not temp:
            temp.append(lis[i][j])
            back_tracking(x+1, i)
            temp.pop()
        elif temp[-1] < lis[i][j]:
            temp.append(lis[i][j])
            back_tracking(x+1, i)
            temp.pop()


for i in range(len(k)):
    back_tracking(0, i)
    if i != len(k)-1:
        print()
