import streamlit as st

col1 , col2 , col3 = st.columns ([1,1,1])

with col2:
    st.title("Tela de Cadastro")
nome = st.text_input("Insira o seu nome de usuário: ")
email = st.text_input("Insira o seu e-mail: ")
senha = st.text_input("Insira sua senha", type = "password")
confirmar_senha = st.text_input("Confirme sua senha:", type = "password")

if st.button("Cadastrar dados"):
    if confirmar_senha == "" or senha == "" or email == "" or nome == "":
        st.error("Preencha todos os campos !!!!!")
    elif confirmar_senha == senha:
        st.success("Usuario cadastrado com sucesso!")
        with open("./pessoa.text","a") as arquivo:
            arquivo.write(f"Nome: {nome} | E - Mail {email}\n")
    elif confirmar_senha != senha:
        st.error("Senha incorreta!!")

 
