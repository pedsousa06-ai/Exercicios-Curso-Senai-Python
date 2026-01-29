def eh_par(numero):
    return numero % 2 == 0

num = int(input("Digite um valor: "))

if eh_par(num):
    print("Seu número é par.")
else:
    print("Seu número é ímpar.")

