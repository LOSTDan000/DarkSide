n = 0
def add(n):
    n = int(input())
    for i in range(1, n + 1):
        for p in range(1, 1 + i):
            print(p, end="")
        print()
add(n)