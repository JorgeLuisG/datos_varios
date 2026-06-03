import pandas as pd
from db import get_connection

def leer_tabla(tabla):

    conn = get_connection()
    df = pd.read_sql(f"SELECT * FROM {tabla}", conn)
    conn.close()
    return df


def cargar_datos():

    return {
        "Contactos Internos": leer_tabla("contactos_internos"),
        "Contratos": leer_tabla("contratos"),
        "Cuil Contratista": leer_tabla("cuil_contratista"),
        "Cronograma Poda": leer_tabla("cronograma_poda"),
        "Certificación Poda": leer_tabla("certificacion_poda"),
    }