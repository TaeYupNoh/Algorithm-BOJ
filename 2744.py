a=list(input())
nlis=[]
for i in a:
    if i.isupper():
        i=i.lower()
        nlis.append(i)
    else :
        i=i.upper()
        nlis.append(i)
print(''.join(nlis))
