import random


numero_magico = random.randint(0,100)
print(f"TRAPAÇA:{numero_magico}")

numero_usuario = int(input("Descubra o número sorteado (0-50): "))

while numero_usuario != numero_magico:

    if numero_magico > numero_usuario:
        print("O número sorteado é maior.")

    elif numero_magico < numero_usuario:
        print("O número sorteado é menor.")

    numero_usuario = int(input(" Tente novamente (0,50): "))
print(" !!!!!!!!!!!!!! Parabens voce acertou !!!!!!!!!!!!!!")