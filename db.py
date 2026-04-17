import psycopg2
import os

def get_connection():
    DATABASE_URL = "postgresql://organizador_db_ahov_user:pd07nJbb0QuBfZAip9tDYH3rVKJZ8sZk@dpg-d7h4v9po3t8c7396v6g0-a.oregon-postgres.render.com/organizador_db_ahov"

    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    return conn
import pandas as pd
from db import get_connection

df = pd.read_csv("data/contrato.csv")

conn = get_connection()
cur = conn.cursor()

for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO contratos (empresa, contratista, descripcion, numero)
        VALUES (%s, %s, %s, %s)
    """, (
        "erlyfsa",  # o lógica según fila
        row[0],
        row[1],
        row[2]
    ))
cur = conn.cursor()

cur.execute("SELECT * FROM tu_tabla;")
rows = cur.fetchall()

for row in rows:
    print(row)
conn.commit()
cur.close()
conn.close()