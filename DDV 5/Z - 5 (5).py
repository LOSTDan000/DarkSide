x=0
def add(x):
    x=int(input())
    i=0 
    z=[]
    while x!=0:
        i+=1
        z.append(x)
        x=int(input())
    print('count of numbers:',i)
add(x)