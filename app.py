import streamlit as st
import streamlit_authenticator as stauth

from search import cargar_datos, buscar

# Usuarios
credentials = {
    "usernames": {
        "admin": {
            "name": "Administrador",
            "password": "pass0"
        },
        "Gurbano": {
            "name": "Gurbano",
            "password": "pass1"
        },
        "Rfornetti": {
            "name": "Rfornetti",
            "password": "pass2"
        },
        "Maguaza": {
            "name": "Maguaza",
            "password": "pass3"
        }
    }
}

authenticator = stauth.Authenticate(
    credentials,
    "buscador_cookie",
    "abcdef123456",
    cookie_expiry_days=30
)

# Login
authenticator.login()

if st.session_state["authentication_status"] is False:
    st.error("Usuario o contraseña incorrectos")
    st.stop()

if st.session_state["authentication_status"] is None:
    st.warning("Ingrese usuario y contraseña")
    st.stop()

# Usuario autenticado
nombre = st.session_state["name"]
usuario = st.session_state["username"]

st.title("Buscador de Tablas")

st.sidebar.write(f"Usuario: {nombre}")

authenticator.logout("Cerrar sesión", "sidebar")

# Cargar datos
cuil_contratista, contratos, cronograma_poda, certificacion_poda = cargar_datos()

dfs = {
    "Cuil Contratista": cuil_contratista,
    "Contratos": contratos,
    "Cronograma Poda": cronograma_poda,
    "Certificación Poda": certificacion_poda
}

opcion = st.sidebar.selectbox(
    "Seleccionar tabla",
    ["Todas"] + list(dfs.keys())
)

query = st.text_input("Buscar...")

if opcion != "Todas":
    dfs = {opcion: dfs[opcion]}

if query:
    resultados = buscar(query, dfs)

    for nombre_tabla, df in resultados:
        st.subheader(nombre_tabla)
        st.dataframe(df, use_container_width=True)
else:
    for nombre_tabla, df in dfs.items():
        st.subheader(nombre_tabla)
        st.dataframe(df, use_container_width=True)