def per(n):
    if len(n) == 0:
        return n
    else:
        return per(n[1:]) + n[0]

number = str(input('Введите число: '))
print('Перевернутое число :',per(number))