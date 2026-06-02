import os
import psycopg2

def get_connection():

    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")

    print("HOST:", host)
    print("PORT:", port)
    print("DB:", dbname)
    print("USER:", user)

    return psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=os.getenv("DB_PASSWORD"),
        sslmode="require"
    )