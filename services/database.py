import pandas as pd
from db import get_connection

def get_table(nombre_tabla):

    conn = get_connection()

    df = pd.read_sql(
        f"SELECT * FROM {nombre_tabla}",
        conn
    )

    conn.close()

    return df