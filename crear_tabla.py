from db import get_connection

def crear_tablas():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE,
            nombre TEXT,
            password TEXT,
            rol TEXT
        );

        CREATE TABLE IF NOT EXISTS contactos_internos (
            id SERIAL PRIMARY KEY,
            sector TEXT,
            usuario TEXT,
            interno TEXT
        );

        CREATE TABLE IF NOT EXISTS contratos (
            id SERIAL PRIMARY KEY
        );

        CREATE TABLE IF NOT EXISTS cronograma_poda (
            id SERIAL PRIMARY KEY
        );

        CREATE TABLE IF NOT EXISTS certificacion_poda (
            id SERIAL PRIMARY KEY
        );

        CREATE TABLE IF NOT EXISTS cuil_contratista (
            id SERIAL PRIMARY KEY
        );
    """)

    conn.commit()
    cur.close()
    conn.close()