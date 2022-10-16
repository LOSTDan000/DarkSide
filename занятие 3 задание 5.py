a=int(input())
b=int(input())
c=int(input())
setmn = {a,b,c}
print(min(setmn, key = lambda i: int(i)))