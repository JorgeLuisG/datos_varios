from db import get_connection


def init_db():

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

    CREATE TABLE IF NOT EXISTS cuil_contratista (
        id SERIAL PRIMARY KEY,
        tipo TEXT,
        empresa TEXT,
        concepto TEXT,
        codigo TEXT
    );

    CREATE TABLE IF NOT EXISTS contratos (
        id SERIAL PRIMARY KEY,
        tipo TEXT,
        empresa TEXT,
        contrato TEXT,
        nro_contrato TEXT
    );

    CREATE TABLE IF NOT EXISTS cronograma_poda (
        id SERIAL PRIMARY KEY,
        tipo TEXT,
        actividad TEXT,
        periodo_inicio TEXT,
        periodo_fin TEXT,
        tension TEXT
    );

    CREATE TABLE IF NOT EXISTS certificacion_poda (
        id SERIAL PRIMARY KEY,
        tipo TEXT,
        cuadricula_distribuidor TEXT,
        labt TEXT,
        lamt TEXT
    );

    CREATE TABLE IF NOT EXISTS contactos_internos (
        id SERIAL PRIMARY KEY,
        sector TEXT,
        usuario TEXT,
        interno TEXT
    );
    """)
   

    conn.commit()

    cur.close()
    conn.close()