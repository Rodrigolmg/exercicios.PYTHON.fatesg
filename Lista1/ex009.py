from time import sleep
from math import trunc
real = float(input('Informe o valor a ser distribuído: R$ '))
print('Processando...')
print('----' * 8)
sleep(1)
cem = real // 100
cincoq = real // 50
dez = real // 10
cinc = real // 5
um = real // 1
print('Notas distribuídas em:')
print('Cem = \033[1;36m{}\033[m \nCinquenta = \033[1;36m{}\033[m \nDez = \033[1;36m{}\033[m'.format(cem, cincoq, dez))
print('Cinco = \033[1;36m{}\033[m \nUm = \033[1;36m{}\033[m'.format(cinc, um))
