i=0
a,b=[],{}
while i<10:
    a.append(int(input())%42)
    i+=1

for j in a:
    b[j]=b.get(j,0)+1

print(len(b.values()))
