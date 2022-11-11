n=int(input())
n=n>>1
s=1
k=0
while s<=n:
    s*=2
    k+=1
print('The highest degree of 2 =',k,'; The result of exponentation =',s,';')