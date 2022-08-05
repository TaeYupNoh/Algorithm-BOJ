# 2163 초콜릿 자르기
n, m = map(int, input().split())
big = max(n, m)
small = min(n, m)
print(small-1+small*(big-1))
