def dits(x, y, x1 ,y1):
    x = int(input())
    y = int(input())
    x1 = int(input())
    y1 = int(input())
    if (x + y + x1 + y1) % 2 == 0:
        print('Да')
    else:
        print('Нет')
x = 0
y = 0
x1 = 0
y1 = 0
dits(x, y, x1, y1)