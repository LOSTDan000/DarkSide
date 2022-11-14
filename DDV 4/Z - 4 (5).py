n = 0
i = 0
z = []
fuck = 1
def add(n,i,z,fuck):
    n = int(input())
    i = 0
    z = []
    fuck = 1
    for i in range(n):
        z.append(i+1)
    print(z)
    i = 1
    for i in range(n):
        z[i] = z[i]**3
        fuck = fuck + z[i]
    print(z)
    print(fuck)
add(n,i,z,fuck)