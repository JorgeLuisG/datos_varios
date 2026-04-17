import streamlit as st
from search import cargar_datos, buscar

st.title("Buscador de Tablas")

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