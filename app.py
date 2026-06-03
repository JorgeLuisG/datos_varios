import streamlit as st
import streamlit_authenticator as stauth

from models.init_db import init_db
from auth import obtener_credenciales, obtener_rol
from services.contactos import get_contactos, create_contacto, update_contacto, delete_contacto

# -------------------
# INIT DB
# -------------------
init_db()

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

user = st.session_state["username"]
rol = obtener_rol(user)

st.sidebar.success(user)
authenticator.logout("Salir", "sidebar")

# -------------------
# DATA
# -------------------
df = get_contactos()

st.title("Contactos Internos")

st.dataframe(df, use_container_width=True)

# -------------------
# CREATE
# -------------------
st.subheader("Agregar")

with st.form("add"):
    sector = st.text_input("Sector")
    usuario = st.text_input("Usuario")
    interno = st.text_input("Interno")

    if st.form_submit_button("Guardar"):
        create_contacto({
            "sector": sector,
            "usuario": usuario,
            "interno": interno
        })
        st.rerun()

# -------------------
# UPDATE
# -------------------
st.subheader("Editar")

id_edit = st.number_input("ID", min_value=1)

with st.form("edit"):
    sector = st.text_input("Sector")
    usuario = st.text_input("Usuario")
    interno = st.text_input("Interno")

    if st.form_submit_button("Actualizar"):
        update_contacto(id_edit, {
            "sector": sector,
            "usuario": usuario,
            "interno": interno
        })
        st.rerun()

# -------------------
# DELETE
# -------------------
st.subheader("Eliminar")

id_del = st.number_input("ID eliminar", min_value=1)

if st.button("Eliminar"):
    delete_contacto(id_del)
    st.rerun()