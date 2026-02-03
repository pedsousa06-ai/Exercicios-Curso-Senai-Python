import streamlit as st

def adicao(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 == 0:
        return "Erro: divisão por zero"
    return n1 / n2


st.title("Calculadora Simples")
st.subheader("Feito com Streamlit")

num1 = st.number_input("Digite o primeiro valor:")
num2 = st.number_input("Digite o segundo valor:")

opcao = st.selectbox(
    "Qual operação deseja realizar?",
    ("Soma", "Subtração", "Multiplicação", "Divisão")
)

try:
    if st.button("Calcular"):
        if opcao == "Soma":
            resultado = adicao(num1, num2)

        elif opcao == "Subtração":
            resultado = subtrair(num1, num2)

        elif opcao == "Multiplicação":
            resultado = multiplicar(num1, num2)

        elif opcao == "Divisão":
            resultado = dividir(num1, num2)

        st.success(f"Resultado: {resultado}")

except Exception as e:
    st.error("Ocorreu um erro")