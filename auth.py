from db import get_connection

def obtener_credenciales():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT username, nombre, password
        FROM usuarios
    """)

    rows = cur.fetchall()

    credentials = {"usernames": {}}

    for u, n, p in rows:
        credentials["usernames"][u] = {
            "name": n,
            "password": p
        }

    conn.close()
    return credentials


def obtener_rol(username):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT rol FROM usuarios WHERE username=%s", (username,))
    row = cur.fetchone()

    conn.close()

    return row[0] if row else None