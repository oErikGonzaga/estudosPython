# Estruturas Condicionais - else

print("Códigos de compra: 5222, 5333, 5444")
cod_compra = int(input("Insira um código de compra: "))

if cod_compra == 5222:
    print("Compra à vista.")
elif cod_compra == 5333:
    print("Compra à prazo no boleto.")
elif cod_compra == 5444:
    print("Compra a prazo no Cartão.")
else:
    print("Código não cadastrado.")
