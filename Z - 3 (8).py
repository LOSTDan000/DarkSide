def compare(a, b, c):
    a = int(input())
    b = int(input())
    c = int(input())
    if a == b and a == c and b == c:
        print('3')
    elif a == b or a == c or b == c:
        print('2')
    else:
        print('0')
a = 0
b = 0
c = 0
compare(a, b, c)