god = int(input())
a = god % 4
b = god % 100
c = god % 400
print(a,b,c)
if (a==0 or c==0) and b!=0:
    print('Yes')
else :
    print('No')