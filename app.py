import streamlit as st
from search import cargar_datos, buscar

USUARIOS = {
    "admin": "pass0",
    "Gurbano": "pass1",
    "Rfornetti": "pass2",
    "Maguaza": "pass3"
}

# estado inicial
if "login" not in st.session_state:
    st.session_state["login"] = False
if "usuario" not in st.session_state:
    st.session_state["usuario"] = ""

def login():
    st.title("Login")

    usuario = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        if usuario in USUARIOS and USUARIOS[usuario] == password:
            st.session_state["login"] = True
            st.session_state["usuario"] = usuario
            st.rerun()
        else:
            st.error("Usuario o contraseña incorrectos")

# 🔐 protección
if not st.session_state["login"]:
    login()
    st.stop()

# 👇 recién acá el usuario existe
st.title("Buscador de Tablas")

st.sidebar.write(f"Usuario: {st.session_state['usuario']}")

# logout
if st.sidebar.button("Cerrar sesión"):
    st.session_state["login"] = False
    st.session_state["usuario"] = ""
    st.rerun()

# cargar datos
cuil_contratista, contratos, cronograma_poda, certificacion_poda = cargar_datos()

# menú
opcion = st.sidebar.selectbox(
    "Seleccionar tabla",
    ["Todas", "Cuil Contratista", "Contratos", "Cronograma Poda", "Certificación Poda"]
)

query = st.text_input("Buscar...")

dfs = {
    "Cuil Contratista": cuil_contratista,
    "Contratos": contratos,
    "Cronograma Poda": cronograma_poda,
    "Certificación Poda": certificacion_poda
}

if opcion != "Todas":
    dfs = {opcion: dfs[opcion]}

if query:
    resultados = buscar(query, dfs)

    for nombre, df in resultados:
        st.subheader(nombre)
        st.dataframe(df)
else:
    for nombre, df in dfs.items():
        st.subheader(nombre)
        st.dataframe(df)