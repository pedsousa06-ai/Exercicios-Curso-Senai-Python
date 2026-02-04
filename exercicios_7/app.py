import streamlit as st

st.title("Tabuada Automatica")

def tabuada(n1):
    resultados = []
    i = 1
    while i <= 10:
        resultados.append(f"{n1} x {i} = {n1 * i}")
        i += 1
    return resultados

numero = st.number_input("Digite um número:", value=1, step=1)

if st.button("Gerar tabuada"):
    resultado = tabuada(numero)
    for linha in resultado:
        st.write(linha)
