# 분수찾기
x=int(input())

num=1
plus=2
while x>num:
    num+=plus
    plus+=1

top_down_sum = plus
pre_num=num-plus+1

if top_down_sum%2 == 1:
    print(f'{x-pre_num}/{top_down_sum-(x-pre_num)}')
else:
    print(f'{top_down_sum-(x-pre_num)}/{x-pre_num}')
