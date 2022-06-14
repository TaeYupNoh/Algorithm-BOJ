a=[]
b=list(range(1,31))
for i in range(28):
    a.append(int(input()))
c=[j for j in b if j not in a]
c.sort()
print(c[0])
print(c[1])
