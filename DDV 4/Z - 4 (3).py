a = 0
b = 0
def add(a,b):
    a = int(input())
    b = int(input())
    while a != b:
       a -= 1
       if a % 2 != 0:
           print(a)
add(a,b)