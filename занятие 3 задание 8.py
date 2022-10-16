a = int(input())
b = int(input())
c = int(input())
d = 0
if a==b and b != c :
    print('2')
if b==c and c != a :
    print('2')
if c==a and a != b :
    print('2')
if a != b and b != c and c != a :
    print('0')
if a == b and b == c and c == a :
    print('3')