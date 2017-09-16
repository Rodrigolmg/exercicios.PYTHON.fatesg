from time import sleep
id = int(input('Digite sua idade expressa em dias: '))
print('Analisando...')
print('-=-' * 10)
sleep(1)
ano = id / 365
mes = id / 30
dia = id % 30
print('Você tem:')
print('\033[1;31m{}\033[m anos, \033[1;32m{}\033[m meses e \033[1;33m{}\033[m dias'.format(ano, mes, dia))