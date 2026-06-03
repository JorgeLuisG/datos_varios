import streamlit as st


def mostrar_tabla(df, titulo):
    st.subheader(titulo)
    st.dataframe(
        df,
        use_container_width=True
    )


def formulario_alta(columnas):

    datos = {}

    with st.form("alta"):

        for columna in columnas:

            if columna != "id":
                datos[columna] = st.text_input(columna)

        submit = st.form_submit_button("Guardar")

    return submit, datos


def formulario_edicion(columnas):

    id_registro = st.number_input(
        "ID",
        min_value=1,
        step=1
    )

    datos = {}

    with st.form("edicion"):

        for columna in columnas:

            if columna != "id":
                datos[columna] = st.text_input(columna)

        submit = st.form_submit_button("Actualizar")

    return submit, id_registro, datos


def formulario_eliminar():

    id_registro = st.number_input(
        "ID a eliminar",
        min_value=1,
        step=1
    )

    eliminar = st.button("Eliminar")

    return eliminar, id_registro