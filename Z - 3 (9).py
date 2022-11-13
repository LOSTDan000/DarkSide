def shok(n, m, k):
    n = int(input())
    m = int(input())
    k = int(input())
    if (k % n == 0 or k % m == 0) and (k < n * m):
        print('Да')
    else:
        print("Нет")
n = 0
m = 0
k = 0
shok(n, m, k)