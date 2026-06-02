import streamlit as st
import streamlit_authenticator as stauth

from crear_tabla import crear_tabla_usuarios
from cargar_usuarios import cargar_usuarios_iniciales

from auth import (
    obtener_credenciales,
    obtener_rol
)

from search import (
    cargar_datos,
    buscar
)

# -----------------------------
# Inicialización BD
# -----------------------------

crear_tabla_usuarios()
cargar_usuarios_iniciales()

# -----------------------------
# Credenciales
# -----------------------------

credentials = obtener_credenciales()

# -----------------------------
# Login
# -----------------------------

authenticator = stauth.Authenticate(
    credentials,
    "organizador_cookie",
    "abcdef123456789",
    cookie_expiry_days=30
)

try:
    authenticator.login()
except Exception as e:
    st.error(f"Error login: {e}")
    st.stop()

# -----------------------------
# Estado login
# -----------------------------

if st.session_state.get("authentication_status") is False:
    st.error("Usuario o contraseña incorrectos")
    st.stop()

if st.session_state.get("authentication_status") is None:
    st.warning("Ingrese usuario y contraseña")
    st.stop()

# -----------------------------
# Usuario autenticado
# -----------------------------

username = st.session_state["username"]
nombre = st.session_state["name"]

rol = obtener_rol(username)

st.title("Buscador de Tablas")

st.sidebar.success(f"Usuario: {nombre}")
st.sidebar.write(f"Rol: {rol}")

authenticator.logout(
    "Cerrar sesión",
    "sidebar"
)

# -----------------------------
# Cargar Excels
# -----------------------------

(
    cuil_contratista,
    contratos,
    cronograma_poda,
    certificacion_poda
) = cargar_datos()

dfs = {
    "Cuil Contratista": cuil_contratista,
    "Contratos": contratos,
    "Cronograma Poda": cronograma_poda,
    "Certificación Poda": certificacion_poda
}

# -----------------------------
# Permisos
# -----------------------------

PERMISOS = {
    "admin": [
        "Cuil Contratista",
        "Contratos",
        "Cronograma Poda",
        "Certificación Poda"
    ],

    "usuario": [
        "Contratos",
        "Cronograma Poda"
    ]
}

tablas_permitidas = PERMISOS.get(
    rol,
    []
)

dfs = {
    nombre_tabla: df
    for nombre_tabla, df in dfs.items()
    if nombre_tabla in tablas_permitidas
}

# -----------------------------
# Menú
# -----------------------------

opcion = st.sidebar.selectbox(
    "Seleccionar tabla",
    ["Todas"] + list(dfs.keys())
)

query = st.text_input(
    "Buscar..."
)

# -----------------------------
# Mostrar datos
# -----------------------------

if opcion != "Todas":
    dfs = {
        opcion: dfs[opcion]
    }

if query:

    resultados = buscar(
        query,
        dfs
    )

    for nombre_tabla, df in resultados:

        st.subheader(nombre_tabla)

        st.dataframe(
            df,
            use_container_width=True
        )

else:

    for nombre_tabla, df in dfs.items():

        st.subheader(nombre_tabla)

        st.dataframe(
            df,
            use_container_width=True
        )