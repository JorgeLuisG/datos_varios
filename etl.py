import pandas as pd
from db import get_connection

def importar_csv(tabla, archivo, columnas):

    df = pd.read_csv(archivo)
    df.columns = [c.strip().lower() for c in df.columns]

    conn = get_connection()
    cur = conn.cursor()

    for _, row in df.iterrows():

        valores = [row[c] for c in columnas]

        cur.execute(
            f"""
            INSERT INTO {tabla} ({",".join(columnas)})
            VALUES ({",".join(["%s"] * len(columnas))})
            ON CONFLICT DO NOTHING
            """,
            valores
        )

    conn.commit()
    cur.close()
    conn.close()


def cargar_todo():

    importar_csv(
        "contactos_internos",
        "data/contactos internos.csv",
        ["sector", "usuario", "interno"]
    )

    importar_csv(
        "contratos",
        "data/contratos.csv",
        ["col1", "col2"]  # ajusta a tu CSV real
    )