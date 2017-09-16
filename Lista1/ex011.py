taxa = float(input("Taxa do dólar hoje: ").replace(',', '.'))
compra = float(input("Valor da compra: US$ ").replace(',', '.'))
icms = float(input("Percentual de ICMS: ").replace(',', '.'))
lucro = float(input("Percentual de lucro da empresa: ").replace(',', '.'))

real = compra * taxa
icms_real = (real / 100) * icms
taxa_lucro = (real / 100) * lucro

total = real + icms_real + taxa_lucro

print("Valor total da compra em reais: R$ {:.2f}".format(total).replace('.', ','))
