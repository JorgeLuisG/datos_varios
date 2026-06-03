from db import get_connection


def insert_row(tabla, datos):

    conn = get_connection()
    cur = conn.cursor()

    columnas = list(datos.keys())
    valores = list(datos.values())

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


def update_row(tabla, id_registro, datos):

    conn = get_connection()
    cur = conn.cursor()

    campos = ", ".join(
        [f"{k}=%s" for k in datos.keys()]
    )

    valores = list(datos.values())
    valores.append(id_registro)

    cur.execute(
        f"""
        UPDATE {tabla}
        SET {campos}
        WHERE id=%s
        """,
        valores
    )

    conn.commit()

    cur.close()
    conn.close()


def delete_row(tabla, id_registro):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        f"DELETE FROM {tabla} WHERE id=%s",
        (id_registro,)
    )

    conn.commit()

    cur.close()
    conn.close()