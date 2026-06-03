from db import get_connection

def insertar(tabla, datos):

    conn = get_connection()
    cur = conn.cursor()

    cols = ",".join(datos.keys())
    vals = list(datos.values())

    cur.execute(
        f"INSERT INTO {tabla} ({cols}) VALUES ({','.join(['%s']*len(vals))})",
        vals
    )

    conn.commit()
    cur.close()
    conn.close()


def actualizar(tabla, id_registro, datos):

    conn = get_connection()
    cur = conn.cursor()

    set_clause = ",".join([f"{k}=%s" for k in datos.keys()])
    vals = list(datos.values())
    vals.append(id_registro)

    cur.execute(
        f"UPDATE {tabla} SET {set_clause} WHERE id=%s",
        vals
    )

    conn.commit()
    cur.close()
    conn.close()


def eliminar(tabla, id_registro):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        f"DELETE FROM {tabla} WHERE id=%s",
        (id_registro,)
    )

    conn.commit()
    cur.close()
    conn.close()