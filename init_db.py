from db import get_connection

conn = get_connection()
cur = conn.cursor()

# tabla usuarios
cur.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    usuario TEXT UNIQUE,
    password TEXT,
    empresa TEXT
);
""")

# ejemplo contratos
cur.execute("""
CREATE TABLE IF NOT EXISTS contratos (
    id SERIAL PRIMARY KEY,
    empresa TEXT,
    contratista TEXT,
    descripcion TEXT,
    numero TEXT
);
""")

conn.commit()
cur.close()
conn.close()