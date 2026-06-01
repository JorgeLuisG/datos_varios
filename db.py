import psycopg2


def get_connection():
    DATABASE_URL = "postgresql://organizador_db_ahov_user:pd07nJbb0QuBfZAip9tDYH3rVKJZ8sZk@dpg-d7h4v9po3t8c7396v6g0-a.oregon-postgres.render.com/organizador_db_ahov"

    return psycopg2.connect(
        DATABASE_URL,
        sslmode="require"
    )