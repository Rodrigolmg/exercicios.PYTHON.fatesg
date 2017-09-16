from math import pi
from time import sleep
print('Dados do cilindro: ')
raio = float(input('Informe o raio: '))
alt = float(input('Informe a altura: '))
sleep(1)
print('Analisando...')
print('-' * 35)
sleep(2)
area = 2 * pi * raio * (alt + raio)
vol = pi * (raio ** 2) * alt
print('Raio: \033[1;30m{}\033[m \nAltura: \033[1;30m{}\033[m'.format(raio, alt))
print('Área do cilindro: \033[1;31m{}\033[m \nVolume do cilindro: \033[1;32m{}\033[m'.format(area, vol))