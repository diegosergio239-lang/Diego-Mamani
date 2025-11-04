# IMPORTAMOS Streamlit
# pip install python | python -m install streamlit
import streamlit as st

st.set_page_config(page_title="Mi chat de IA", page_icon="👍")
st.title("Mi primera aplicacion con Streamlit")

nombre = st.text_input("Cual es tu nombre?")
if st.button("Saludar!"):
    st.write(f"Hola {nombre}! Bienvenido a talento tech")

MODELOS = ['llama-3.1-8b-instant', 'llama-3.3-70b-versatile', 'deepseek-r1-distill-llama-70b']

def configurar_pagina():
    st.title("Mi Chat de IA - Diego")
    st.sidebar.title("Configuracion de la IA")

    elegirModelo = st.sidebar.selectbox(
        "Elegi un modelo",
        options = MODELOS,
        index = 0
    )

    return elegirModelo

def crear_usuario_groq():
    clave_secreta = st.secrets["CLAVE_API"]
    return Groq

def configurar_modelo(cliente, modelo, mensajeDeEntrada):
    return cliente.chat.completions.create(
        model = modelo,
        messages = [{"role":"user", "content": mensajeDeEntrada}],
        stream = False
    )

def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []
def crear_usuario_groq():
    clave_secreta = st.secrets["CLAVE_API"]
    return Groq(CLAVE_API = "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")

def configurar_modelo(cliente, modelo, mensajeDeEntrada):
    return cliente.chat.completions.create(
        model = modelo,
        messages = [{"role":"user", "content": mensajeDeEntrada}],
        stream = False
    )

def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

def actualizar_historial(rol, contenido, avatar):
    st.session_state.mensajes.append({"role": rol, "content": contenido, "avatar": avatar})

def mostrar_historial():
    for mensaje in st.session_state.mensajes:
        with st.chat_message(mensaje["role"], avatar= mensaje["avatar"]) : st.markdown(mensaje["content"])

def area_chat():
    contenedorDelChat = st.container(height=400, border= True)
    with contenedorDelChat: mostrar_historial()


clienteUsuario = crear_usuario_groq()
inicializar_estado()
modelo = configurar_pagina()
area_chat()
mensaje = st.chat_input("Escribi tu mensaje:")

if mensaje:
    actualizar_historial("user", mensaje, "😁")
    chat_completo = configurar_modelo(clienteUsuario, modelo, mensaje)
    actualizar_historial("assistant", chat_completo, "🤖")
    st.rerun() 


#Agregamos este codigo al final

# Correr streamlit con la terminal de Python
# python -m streamlit run MiChat.py (aca deben ingresar el nombre del archivo)

