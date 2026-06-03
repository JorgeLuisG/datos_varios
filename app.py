import streamlit as st
import streamlit_authenticator as stauth

from crear_tabla import crear_tablas
from search import cargar_datos
from auth import obtener_credenciales, obtener_rol
from crud import insertar, actualizar, eliminar

# -------------------
# INIT BD
# -------------------
crear_tablas()

# -------------------
# LOGIN
# -------------------
credentials = obtener_credenciales()

authenticator = stauth.Authenticate(
    credentials,
    "cookie",
    "secret",
    cookie_expiry_days=30
)

authenticator.login()

if st.session_state.get("authentication_status") is False:
    st.error("Login incorrecto")
    st.stop()

if st.session_state.get("authentication_status") is None:
    st.warning("Login requerido")
    st.stop()

username = st.session_state["username"]
rol = obtener_rol(username)

st.sidebar.success(f"Usuario: {username}")
authenticator.logout("Salir", "sidebar")

# -------------------
# DATOS
# -------------------
dfs = cargar_datos()

tabla = st.sidebar.selectbox("Tabla", list(dfs.keys()))
df = dfs[tabla]

st.title(tabla)
st.dataframe(df, use_container_width=True)

# -------------------
# CRUD
# -------------------
st.divider()

st.subheader("Agregar")

with st.form("add"):
    data = {}

    for col in df.columns:
        if col != "id":
            data[col] = st.text_input(col)

    if st.form_submit_button("Guardar"):
        insertar(tabla.lower().replace(" ", "_"), data)
        st.rerun()

st.subheader("Editar")

id_edit = st.number_input("ID", min_value=1)

with st.form("edit"):
    data = {}

    for col in df.columns:
        if col != "id":
            data[col] = st.text_input(col)

    if st.form_submit_button("Actualizar"):
        actualizar(tabla.lower().replace(" ", "_"), id_edit, data)
        st.rerun()

st.subheader("Eliminar")

id_del = st.number_input("ID eliminar", min_value=1)

if st.button("Eliminar"):
    eliminar(tabla.lower().replace(" ", "_"), id_del)
    st.rerun()