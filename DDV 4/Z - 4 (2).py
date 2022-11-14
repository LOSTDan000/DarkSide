a = 0
b = 0
def add(a,b):
    a = int(input())
    b = int(input())
    if a < b :
        print('')
        print(a)
        while a != b:
            a += 1
            print(a)
    elif a > b :
        print('')
        print(a)
        while a != b:
            a -= 1
            print(a)
add(a,b)