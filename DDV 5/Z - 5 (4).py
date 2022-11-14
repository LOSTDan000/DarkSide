x = 0
y = 0
def add(x,y):
    x=int(input())
    y=int(input())
    i=1
    while x<y:
        x=x*1.1
        i=i+1
    print('The number of a day is:',i)
add(x,y)