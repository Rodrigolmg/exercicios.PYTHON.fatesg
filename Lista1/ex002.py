from math import sqrt
m = int(input('Digite o primeiro valor: '))
n = int(input('Digite o segundo valor: '))
l1 = (m ** 2) - (n ** 2)
l2 = 2 * m * n
h = sqrt((m ** 2) + (n ** 2))
print('\033[1;30mLado 1: {}\033[m \n\033[1;31mLado 2: {}\033[m \n\033[1;32mHipotenusa: {}\033[m'.format(l1, l2, h))