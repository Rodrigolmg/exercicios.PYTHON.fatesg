from math import sqrt
l1 = float(input('Digite o valor do lado 1: '))
l2 = float(input('Digite o valor do lado 2: '))
l3 = float(input('Digite o valor do lado 3: '))
t = (l1 + l2 + l3)/ 2
area = sqrt(t * (t - l1) * (t - l2) * (t - l3))
print('Área do triângulo = \033[1;34m{}\033[m'.format(area))