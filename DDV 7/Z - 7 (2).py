n=8
def add(n):
    D = []
    n = 8
    i = 0
    for i in range(n):
        D.append(int(input()))
    print('')
    print('Оригинальный Массив',D)
    print('')
    for i in range(n):
        if D[i] <  15 :
            D[i] *= 2
    print('Измененный Массив',D)
add(n)