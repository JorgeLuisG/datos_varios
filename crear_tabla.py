from db import get_connection


def crear_tabla_usuarios():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            nombre VARCHAR(100) NOT NULL,
            password VARCHAR(255) NOT NULL,
            rol VARCHAR(50) NOT NULL
        );
    """)

    conn.commit()

    cur.close()
    conn.close()

    print("Tabla usuarios verificada")