dict={4.3:'A+',4.0:'A0',3.7:'A-',3.3:'B+',3.0:'B0',2.7:'B-',2.3:'C+',2.0:'C0',1.7:'C-',1.3:'D+',1.0:'D0',0.7:'D-',0.0:'F'}
inp=input()
vlis=list(dict.values())
klis=list(dict.keys())
for i in range(13):
    if inp == vlis[i]:
        print(klis[i])
