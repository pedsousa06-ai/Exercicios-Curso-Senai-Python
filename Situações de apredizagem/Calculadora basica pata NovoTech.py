# Funções para operações matemáticas

def adicao(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 == 0:
        return "Erro: divisão por zero não é permitida!"
    return n1 / n2


# Painel de escolha de qual operação irá desejar

titulo = " CALCULADORA BASICA NOVOTECH "

while True:

    print("\n" + "=" * 50)
    print(titulo.center(50))
    print("=" * 50)

    print(f"{'1. -> Adição':<25} {'2. -> Subtração':<25}")
    print(f"{'3. -> Multiplicação':<25} {'4. -> Divisão':<25}")
    print(f"{'0. -> Sair':<25}")

    try:
        opcao = int(input("\nDigite uma das opções: "))
    except ValueError:
        print("Erro: Digite apenas números (0 a 4)!")
        continue


    if opcao == 0:
        print("Saindo da calculadora...........")
        break

    if opcao < 0 or opcao > 4:
        print("Opção inválida! Escolha de 0 a 4.")
        continue

    # Pedir os números
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    # Executar a operação
    if opcao == 1:
        print("Resultado:", adicao(n1, n2))

    elif opcao == 2:
        print("Resultado:", subtrair(n1, n2))

    elif opcao == 3:
        print("Resultado:", multiplicar(n1, n2))

    elif opcao == 4:
        print("Resultado:", dividir(n1, n2))

