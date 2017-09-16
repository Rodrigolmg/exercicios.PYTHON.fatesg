idade = int(input('Informe sua idade: '))
batidas = 31557600 * idade
print('Se você viver \033[1;36m{}\033[m anos, seu coração baterá \033[1;33m{}\033[m vezes.'.format(idade, batidas))