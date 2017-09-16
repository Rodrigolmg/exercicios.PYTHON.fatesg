from time import sleep
num = int(input("Digite um valor: "))
centena = (num % 10) * 100
dezena = ((num // 10) % 10) * 10
unidade = (num // 100)
invertido = centena + dezena + unidade
print("Invertendo...")
sleep(1)
print("Número invertido: \033[1;34m{}\033[m".format(invertido))