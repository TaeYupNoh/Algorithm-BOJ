# 2530 인공지능 시계


h, m, s = map(int, input().split())
d = int(input())

s += d
m += s//60
h += m//60

print(h, m, s)

# 일일이 계산해준 버전
h, m, s = map(int, input().split())
d = int(input())

s += d % 60
d = d//60
if s >= 60:
    s -= 60
    m += 1

m += d % 60
d = d // 60
if m >= 60:
    m -= 60
    h += 1

h += d % 24
if h >= 24:
    h -= 24

print(h, m, s)

