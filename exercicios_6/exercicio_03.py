titulo = "CONVERSOR DE TEMPERATURA"
saida = " PRESSIONE ZERO PARA SAIR"
espaço = "                         "
cf = "1 -> Celsius para Fahrenheit"
fc = "2 -> Fahreinheit para Celsius"
while True:

    print("\n" + "=" * 50)
    print(titulo.center(50))
    print(espaço)
    print(cf.center(50))
    print(fc.center(50))
    print("\n" + "=" * 50)
    print(espaço)
    print(saida.center(50))
    print("\n" + "=" * 50)
    try:
        opcao = int(input("Escolha: "))

        if opcao == 0:
            print("Saindo...")
            break

        temperatura = float(input("Digite a temperatura: "))

        if opcao == 1:
            resultado = (temperatura * 9/5) + 32
            print(f"{temperatura}°C = {resultado:.2f}°F")

        elif opcao == 2:
            resultado = (temperatura - 32) * 5/9
            print(f"{temperatura}°F = {resultado:.2f}°C")

        else:
            print("Opção inválida!")

    except ValueError:
        print("Erro: digite somente números válidos!")
