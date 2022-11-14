import math
hip2 = 0
hip1 = 0
# Функции для Гипотенуз
def tr1(k1,k2,hip1):
    hip1 = k1**2 + k2**2
    hip1 = math.sqrt(hip1)
    return hip1
def tr2(k3,k4,hip2):
    hip2 = k3**2 + k4**2
    hip2 = math.sqrt(hip2)
    return hip2
# Присвоение переменным значений для облегчения работы
h1 = tr1(int(input()),int(input()),0)
h2 = tr2(int(input()),int(input()),0)
# Условия для задания
if h1 > h2 :
    print('Гипотенуза 1-ого треугольника больше 2-ого')
elif h1 == h2 :
    print('Гипотенузы равны по величине')
else :
    print('Гипотенуза 2-ого треугольника больше 1-ого')