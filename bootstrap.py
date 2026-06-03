import pandas as pd
from pathlib import Path

from db import get_connection


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


TABLAS = [
    {
        "tabla": "cuil_contratista",
        "archivo": DATA_DIR / "cuil contratista.csv",
        "sep": ","
    },
    {
        "tabla": "contratos",
        "archivo": DATA_DIR / "contrato.csv",
        "sep": ","
    },
    {
        "tabla": "cronograma_poda",
        "archivo": DATA_DIR / "cronograma poda.csv",
        "sep": ","
    },
    {
        "tabla": "certificacion_poda",
        "archivo": DATA_DIR / "certificacion poda.csv",
        "sep": ";"
    },
    {
        "tabla": "contactos_internos",
        "archivo": DATA_DIR / "contactos internos.csv",
        "sep": ";"
    }
]


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


def importar_tabla(tabla, archivo, sep):

    if not archivo.exists():
        print(f"Archivo no encontrado: {archivo}")
        return

    print(f"Importando {tabla}")

    df = pd.read_csv(
        archivo,
        sep=sep
    )

    # normalizar nombres de columnas
    df.columns = [
        col.strip().lower()
        .replace(" ", "_")
        .replace("-", "_")
        for col in df.columns
    ]

    conn = get_connection()
    cur = conn.cursor()

    columnas = list(df.columns)

    placeholders = ",".join(
        ["%s"] * len(columnas)
    )

    columnas_sql = ",".join(columnas)

    sql = f"""
        INSERT INTO {tabla}
        ({columnas_sql})
        VALUES ({placeholders})
    """

    for _, row in df.iterrows():

        valores = []

        for columna in columnas:

            valor = row[columna]

            if pd.isna(valor):
                valor = None

            valores.append(valor)

        cur.execute(
            sql,
            valores
        )

    conn.commit()

    cur.close()
    conn.close()

    print(
        f"{len(df)} registros cargados en {tabla}"
    )


def inicializar_datos():

    for item in TABLAS:

        tabla = item["tabla"]

        try:

            if tabla_vacia(tabla):

                importar_tabla(
                    tabla,
                    item["archivo"],
                    item["sep"]
                )

            else:

                print(
                    f"{tabla}: ya contiene datos"
                )

        except Exception as e:

            print(
                f"Error en {tabla}: {e}"
            )