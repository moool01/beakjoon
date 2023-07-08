E,S,M,cnt =1,1,1,1

a,b,c = map(int,input().split())

while(True):
    if a==E and b==S and c==M :
        break
    E+=1 ; S+=1 ; M+=1; cnt+=1
    if E>=16 :
        E-=15
    if S>=29 :
        S-=28
    if M>=20 :
        M-=19

print(cnt)