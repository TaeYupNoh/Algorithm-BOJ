# 셀프 넘버

def self_num(x):
    x=x+sum(map(int,str(x)))
    return x

no_self_num = set()

for n in range(1,10001):
    no_self_num.add(self_num(n))

for i in range(1,10001):
    if i not in no_self_num:
        print(i)