# CONVERSORES DE MOEDA (LÓGICA)

# Converte Real para outras moedas
def real_para_dolar(reais):
    return reais / 5.20

def real_para_euro(reais):
    return reais / 5.60

def real_para_iene(reais):
    return reais / 0.034

def real_para_libras(reais):
    return reais / 6.70

def real_para_peso_argentino(reais):
    return reais / 0.0062


# Converte outras moedas para Real
def dolar_para_real(valor):
    return valor * 5.20

def euro_para_real(valor):
    return valor * 5.60

def iene_para_real(valor):
    return valor * 0.034

def libras_para_real(valor):
    return valor * 6.70

def peso_argentino_para_real(valor):
    return valor * 0.0062


# PAINEL DE CONTROLE (INTERFACE)


titulo = "SISTEMA DE CONVERSÃO MONETÁRIA"

while True:
    # Exibição do menu com espaçamento tabular
    print("\n" + "=" * 50)
    print(titulo.center(50))
    print("=" * 50)
    print(f"{'1. Real -> Dólar':<25} {'6. Dólar -> Real':<25}")
    print(f"{'2. Real -> Euro':<25} {'7. Euro -> Real':<25}")
    print(f"{'3. Real -> Iene':<25} {'8. Iene -> Real':<25}")
    print(f"{'4. Real -> Libras':<25} {'9. Libras -> Real':<25}")
    print(f"{'5. Real -> Peso Arg.':<25} {'10. Peso Arg. -> Real':<25}")
    print("-" * 50)
    print("0. Sair")
    print("-" * 50)

    opcao = input("Escolha a opção desejada: ")

    if opcao == '0':
        print("\nFinalizando programa... Até logo!")
        break

    # Verifica se a opção existe antes de pedir o valor
    opcoes_validas = [str(i) for i in range(1, 11)]
    
    if opcao in opcoes_validas:
        try:
            print("") # Espaço em branco
            valor = float(input("Digite o valor para conversão: "))
            print("-" * 20)

            if opcao == '1':
                print(f"Resultado: $ {real_para_dolar(valor):.2f} (USD)")

            elif opcao == '2':
                print(f"Resultado: € {real_para_euro(valor):.2f} (EUR)")

            elif opcao == '3':
                print(f"Resultado: ¥ {real_para_iene(valor):.2f} (JPY)")

            elif opcao == '4':
                print(f"Resultado: £ {real_para_libras(valor):.2f} (GBP)")

            elif opcao == '5':
                print(f"Resultado: $ {real_para_peso_argentino(valor):.2f} (ARS)")

            elif opcao == '6':
                print(f"Resultado: R$ {dolar_para_real(valor):.2f} (BRL)")

            elif opcao == '7':
                print(f"Resultado: R$ {euro_para_real(valor):.2f} (BRL)")

            elif opcao == '8':
                print(f"Resultado: R$ {iene_para_real(valor):.2f} (BRL)")

            elif opcao == '9':
                print(f"Resultado: R$ {libras_para_real(valor):.2f} (BRL)")

            elif opcao == '10':
                print(f"Resultado: R$ {peso_argentino_para_real(valor):.2f} (BRL)")
            
            print("-" * 20)

        except Exception as e:
            print(f"\n[ERRO] Digite apenas números válidos! {e}")
    else:
        print("\n[ERRO] Opção inválida! Tente novamente.")


