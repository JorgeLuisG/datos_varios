import pandas as pd
from db import get_connection


def tabla_vacia(nombre_tabla):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        f"SELECT COUNT(*) FROM {nombre_tabla}"
    )

    cantidad = cur.fetchone()[0]

    cur.close()
    conn.close()

    return cantidad == 0


def importar_contactos():

    df = pd.read_csv(
        "data/contactos internos.csv",
        sep=";"
    )

    conn = get_connection()
    cur = conn.cursor()

    for _, row in df.iterrows():

        cur.execute("""
            INSERT INTO contactos_internos (
                sector,
                usuario,
                interno
            )
            VALUES (%s,%s,%s)
        """, (
            str(row["Sector"]),
            str(row["Usuario"]),
            str(row["Interno"])
        ))

    conn.commit()

    cur.close()
    conn.close()


def inicializar_datos():

    if tabla_vacia("contactos_internos"):
        importar_contactos()
        print("Contactos cargados")
    else:
        print("Contactos ya existen")