# 15654 N과 M(5)
n, m = map(int, input().split())
lis = list(map(int, input().split()))
lis.sort()

temp = []


def back_tracking(x):
    if x == m:
        print(*temp)
        return

    for i in range(len(lis)):
        if lis[i] not in temp:
            temp.append(lis[i])
            back_tracking(x+1)
            temp.pop()


back_tracking(0)
