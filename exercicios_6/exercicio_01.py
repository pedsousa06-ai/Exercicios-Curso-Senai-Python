while True:
    print("\n=== CÁLCULO DE IMC ===")

    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))

        if peso <= 0 or altura <= 0:
            print("Erro: peso e altura devem ser maiores que 0.")
            continue

        imc = peso / (altura ** 2)
        print(f"Seu IMC é: {imc:.2f}")

        if imc < 18.5:
            print("Classificação: Abaixo do peso")
        elif imc < 25:
            print("Classificação: Peso normal")
        elif imc < 30:
            print("Classificação: Sobrepeso")
        else:
            print("Classificação: Obesidade")

        break

    except ValueError:
        print("Erro: digite valores numéricos válidos!")