import streamlit as st
from search import cargar_datos, buscar
USUARIOS = {
    "admin": "pass0",
    "Gurbano": "pass1",
    "isora": "pass2"
}

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
st.title("Buscador de Tablas")
st.sidebar.write(f"Usuario: {st.session_state['usuario']}")
if "login" not in st.session_state:
    st.session_state["login"] = False

if not st.session_state["login"]:
    login()
    st.stop()
st.sidebar.write(f"Usuario: {st.session_state['usuario']}")
# cargar datos
cuil_contratista, contratos, cronograma_poda, certificacion_poda = cargar_datos()

# menú lateral
opcion = st.sidebar.selectbox(
    "Seleccionar tabla",
    ["Todas", "Cuil Contratista", "Contratos", "Cronograma Poda", "Certificación Poda"]
)

query = st.text_input("Buscar...")

# diccionario base
dfs = {
    "Cuil Contratista": cuil_contratista,
    "Contratos": contratos,
    "Cronograma Poda": cronograma_poda,
    "Certificación Poda": certificacion_poda
}

# filtrar según menú
if opcion != "Todas":
    dfs = {opcion: dfs[opcion]}

# búsqueda
if query:
    resultados = buscar(query, dfs)

    for nombre, df in resultados:
        st.subheader(nombre)
        st.dataframe(df)
else:
    # mostrar sin búsqueda
    for nombre, df in dfs.items():
        st.subheader(nombre)
        st.dataframe(df)