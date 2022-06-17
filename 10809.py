from string import ascii_lowercase
a=list(ascii_lowercase)
b=input()
d=[]
for i in a:
    c=-1
    for j in range(len(b)):
        if b[j]==i and c==-1:
            c=j
    d.append(c)
print(*d)
