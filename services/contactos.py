import pandas as pd
from db import get_connection

# READ
def get_contactos():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM contactos_internos", conn)
    conn.close()
    return df

# CREATE
def create_contacto(data):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO contactos_internos (sector, usuario, interno)
        VALUES (%s, %s, %s)
    """, (data["sector"], data["usuario"], data["interno"]))

    conn.commit()
    conn.close()

# UPDATE
def update_contacto(id_, data):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE contactos_internos
        SET sector=%s, usuario=%s, interno=%s
        WHERE id=%s
    """, (data["sector"], data["usuario"], data["interno"], id_))

    conn.commit()
    conn.close()

# DELETE
def delete_contacto(id_):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM contactos_internos WHERE id=%s", (id_,))

    conn.commit()
    conn.close()