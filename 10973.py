# 10973 이전 순열
n = int(input())
lis = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if lis[i-1] > lis[i]:
        for j in range(n-1, 0, -1):
            if lis[i-1] > lis[j]:
                lis[i-1], lis[j] = lis[j], lis[i-1]
                lis = lis[:i]+sorted(lis[i:], reverse=True)
                print(*lis)
                quit()

print(-1)
