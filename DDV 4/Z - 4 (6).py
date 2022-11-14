n = 0
fuck = 1
def add(n,fuck):
    n = int(input())
    fuck = 1
    while n > 1:
        fuck = fuck * n
        n -= 1
    print(fuck)
add(n,fuck)