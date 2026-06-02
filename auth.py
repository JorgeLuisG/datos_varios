from db import get_connection


def obtener_credenciales():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            username,
            nombre,
            password
        FROM usuarios
    """)

    rows = cur.fetchall()

    credentials = {
        "usernames": {}
    }

    for username, nombre, password in rows:
        credentials["usernames"][username] = {
            "name": nombre,
            "password": password
        }

    cur.close()
    conn.close()

    return credentials


def obtener_rol(username):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT rol
        FROM usuarios
        WHERE username = %s
    """, (username,))

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row:
        return row[0]

    return None