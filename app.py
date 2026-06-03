import streamlit as st
import streamlit_authenticator as stauth

from models.init_db import init_db
from bootstrap import inicializar_datos

from auth import (
    obtener_credenciales,
    obtener_rol
)

from services.database import get_table

from services.crud import (
    insert_row,
    update_row,
    delete_row
)

# ----------------------------------
# INICIALIZACIÓN
# ----------------------------------

init_db()
inicializar_datos()

# ----------------------------------
# LOGIN
# ----------------------------------

credentials = obtener_credenciales()

authenticator = stauth.Authenticate(
    credentials,
    "organizador_cookie",
    "abcdef123456789",
    cookie_expiry_days=30
)

authenticator.login()

if st.session_state.get("authentication_status") is False:
    st.error("Usuario o contraseña incorrectos")
    st.stop()

if st.session_state.get("authentication_status") is None:
    st.warning("Ingrese usuario y contraseña")
    st.stop()

username = st.session_state["username"]
nombre = st.session_state["name"]

rol = obtener_rol(username)

# ----------------------------------
# SIDEBAR
# ----------------------------------

st.sidebar.success(f"Usuario: {nombre}")
st.sidebar.write(f"Rol: {rol}")

authenticator.logout(
    "Cerrar sesión",
    "sidebar"
)

# ----------------------------------
# TABLAS DISPONIBLES
# ----------------------------------

TABLAS = {
    "Cuil Contratista": "cuil_contratista",
    "Contratos": "contratos",
    "Cronograma Poda": "cronograma_poda",
    "Certificación Poda": "certificacion_poda",
    "Contactos Internos": "contactos_internos"
}

tabla_nombre = st.sidebar.selectbox(
    "Seleccionar tabla",
    list(TABLAS.keys())
)

tabla_db = TABLAS[tabla_nombre]

# ----------------------------------
# CARGAR DATOS
# ----------------------------------

df = get_table(tabla_db)

st.title(tabla_nombre)

st.write(f"Registros encontrados: {len(df)}")

# ----------------------------------
# PESTAÑAS
# ----------------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "Datos",
    "Agregar",
    "Editar",
    "Eliminar"
])

# ----------------------------------
# DATOS
# ----------------------------------

with tab1:

    st.dataframe(
        df,
        use_container_width=True
    )

# ----------------------------------
# AGREGAR
# ----------------------------------

with tab2:

    st.subheader("Agregar registro")

    columnas = [
        c for c in df.columns
        if c != "id"
    ]

    with st.form("agregar"):

        datos = {}

        for columna in columnas:
            datos[columna] = st.text_input(columna)

        guardar = st.form_submit_button(
            "Guardar"
        )

        if guardar:

            insert_row(
                tabla_db,
                datos
            )

            st.success(
                "Registro agregado"
            )

            st.rerun()

# ----------------------------------
# EDITAR
# ----------------------------------

with tab3:

    st.subheader("Editar registro")

    id_editar = st.number_input(
        "ID",
        min_value=1,
        step=1
    )

    with st.form("editar"):

        datos = {}

        for columna in columnas:
            datos[columna] = st.text_input(columna)

        actualizar = st.form_submit_button(
            "Actualizar"
        )

        if actualizar:

            update_row(
                tabla_db,
                id_editar,
                datos
            )

            st.success(
                "Registro actualizado"
            )

            st.rerun()

# ----------------------------------
# ELIMINAR
# ----------------------------------

with tab4:

    st.subheader("Eliminar registro")

    id_eliminar = st.number_input(
        "ID a eliminar",
        min_value=1,
        step=1,
        key="delete_id"
    )

    if st.button("Eliminar"):

        delete_row(
            tabla_db,
            id_eliminar
        )

        st.success(
            "Registro eliminado"
        )

        st.rerun()