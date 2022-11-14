n=0
i=0
z=[]
summ = 0
def add(n,i,z,summ):
    n = int(input())
    i = 0
    z = []
    summ = 0
    for i in range(n):
        z.append(int(input()))
    print(z)
    i = 1
    for (i) in range(n):
        summ = summ + z[i]
    print(summ)
add(n,i,z,summ)