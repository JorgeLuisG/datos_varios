import pandas as pd
from db import get_connection

TABLAS = [
    (
        "cuil_contratista",
        "data/cuil contratista.csv",
        ","
    ),
    (
        "contratos",
        "data/contrato.csv",
        ","
    ),
    (
        "cronograma_poda",
        "data/cronograma poda.csv",
        ","
    ),
    (
        "certificacion_poda",
        "data/certificacion poda.csv",
        ";"
    ),
    (
        "contactos_internos",
        "data/contactos internos.csv",
        ";"
    )
]

conn = get_connection()
cur = conn.cursor()

for tabla, archivo, sep in TABLAS:

    print(f"Importando {tabla}")

    df = pd.read_csv(
        archivo,
        sep=sep
    )

    # normalizar nombres
    df.columns = [
        c.strip().lower()
        for c in df.columns
    ]

    # limpiar tabla
    cur.execute(
        f"TRUNCATE TABLE {tabla} RESTART IDENTITY"
    )

    columnas = list(df.columns)

    for _, row in df.iterrows():

        valores = [
            str(row[c])
            if pd.notna(row[c])
            else None
            for c in columnas
        ]

        cur.execute(
            f"""
            INSERT INTO {tabla}
            ({','.join(columnas)})
            VALUES ({','.join(['%s']*len(columnas))})
            """,
            valores
        )

conn.commit()

cur.close()
conn.close()

print("Importación finalizada")