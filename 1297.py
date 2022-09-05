# TV 크기
d, h, w = map(int, input().split())

ratio = d/((h ** 2 + w ** 2) ** 0.5)
print(int(h * ratio), int(w * ratio))
