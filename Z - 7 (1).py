D = []
print('Введите количество элементов множества')
n = int(input())
i = 0
summa = 0
for i in range(n):
    D.append(int(input()))
print('')
print(D)
print('')
for i in range(n):
    if i % 2 != 0 :
        summa += D[i]
print('Сумма элементов с нечетными индексами =',summa)