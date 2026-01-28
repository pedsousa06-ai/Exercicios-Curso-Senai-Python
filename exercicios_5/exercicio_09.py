def soma():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("Resultado da soma:", n1 + n2)


def verificar_par():
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("O número é PAR")
    else:
        print("O número é ÍMPAR")


def menu():
    opcao = 0

    while opcao != 3:
        print("-------------------------")
        print("\n-----    MENU 0   -----")
        print("      1 - Soma           ")
        print("    2 - Verificar par    ")
        print("      3 - Sair           ")
        print("-------------------------")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            soma()
        elif opcao == 2:
            verificar_par()
        elif opcao == 3:
            print("Saindo do programa...")
        else:
            print("Opção inválida")


menu()
