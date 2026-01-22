i = 0
contador = 0

valor = int(input("Digite um valor / -1 para sair: "))

while valor != -1:
    i += valor
    contador += 1
    valor = int(input("Digite um valor / -1 para sair: "))

if contador > 0:
    media = i / contador
    print(f"A média dos números é {media}")
else:
    print("Nenhum número válido foi digitado.")