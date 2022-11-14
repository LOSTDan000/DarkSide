frst = 0
pos = 0
def add(frst,pos):
    frst=int(input())
    pos=int(input())
    s=0
    while pos!=0:
        if pos>frst:
            s+=1
            frst=pos
            pos=int(input())
    print('count of numbers, overtaking previous one is:',s)
add(frst,pos)