# 크로아티아 알파벳
import string

inp=input()
alp=[i for i in string.ascii_lowercase]
cro_2=['c=','c-','d-','lj','nj','s=','z=']
cro_3=['dz=']

cnt=0
cro2_cnt=0
cro3_cnt=0
for i in range(len(inp)):
    if inp[i] in alp:
        cnt+=1
    if inp[i:i+2] in cro_2:
        cro2_cnt+=1
        if inp[i] in alp:
            cnt-=1
        if inp[i+1] in alp:
            cnt-=1
    if inp[i:i+3] in cro_3:
        cro3_cnt+=1
        cnt-=2

print(cnt+cro2_cnt+cro3_cnt)
