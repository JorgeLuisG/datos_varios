import streamlit_authenticator as stauth
from db import get_connection

def cargar_usuarios_iniciales():
    passwords = [
        "pass0",
        "pass1",
        "pass2",
        "pass3"
    ]

    hashed_passwords = stauth.Hasher(passwords).generate()

    usuarios = [
        ("admin", "Administrador", hashed_passwords[0], "admin"),
        ("Gurbano", "Gurbano", hashed_passwords[1], "usuario"),
        ("Rfornetti", "Rfornetti", hashed_passwords[2], "usuario"),
        ("Maguaza", "Maguaza", hashed_passwords[3], "usuario")
    ]

    conn = get_connection()
    cur = conn.cursor()

    for usuario in usuarios:
        cur.execute("""
            INSERT INTO usuarios (
                username,
                nombre,
                password,
                rol
            )
            VALUES (%s,%s,%s,%s)
            ON CONFLICT (username)
            DO NOTHING
        """, usuario)

    conn.commit()
    cur.close()
    conn.close()