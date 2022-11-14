n=0
def add(n):
    n = int(input())
    x = 1
    f = 0
    summa = 0
    for i in range(1, n + 1):
        y = x
        x = y + f
        f = y
        summa = summa + y
    print(summa)
add(n)