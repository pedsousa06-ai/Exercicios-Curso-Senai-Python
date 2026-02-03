while True:
    print("\n=== TABUADA ===")

    try:
        numero = int(input("Digite um número para ver a tabuada: "))

        if numero < 0:
            print("Erro: digite um número positivo (0 ou maior).")
            continue

        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")

        break

    except ValueError:
        print("Erro: digite apenas números inteiros!")
