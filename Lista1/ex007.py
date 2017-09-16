from time import sleep
from math import pow
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
print('Fazendo cálculos...')
print('-//-' * 20)
sleep(1)
r = pow((a + b), 2)
print('R = \033[1;31m{}\033[m'.format(r))
sleep(1)
s = pow((b + c), 2)
print('S = \033[1;32m{}\033[m'.format(s))
sleep(1)
d = (r + s) / 2
print('D = \033[1;34m{}\033[m'.format(d))
