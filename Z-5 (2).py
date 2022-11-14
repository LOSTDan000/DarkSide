N = 0
def add(N):
    N=int(input())
    deli=2
    while N%deli!=0:
        deli+=1
    print(deli)
add(N)
