from db import get_connection


def cargar_usuarios_iniciales():

    usuarios = [
        (
            "admin",
            "Administrador",
            "$2b$12$lTk2/hDZprrnwwbp1eL5cuCDjgx1tIPo2Mfx8wIpuFG.oJxezeYLO",
            "admin"
        ),
        (
            "Gurbano",
            "Gurbano",
            "$2b$12$BjXgNz4j6426z1eh8PmryOUKS0BYnlCrWv8.9OdEFGmzzC6/O7FUu",
            "usuario"
        ),
        (
            "Rfornetti",
            "Rfornetti",
            "$2b$12$Qe8wEi8X8jU.WghBRE9ykuUoXuynXy3o03tj4jN0UHwg7EpvkRw4.",
            "usuario"
        ),
        (
            "Maguaza",
            "Maguaza",
            "$2b$12$15ml7O2oguYjh1AqAYJuJe52eADK9UAP/9OoGjyB.iCxikO//ARkm",
            "usuario"
        )
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
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (username)
            DO NOTHING
        """, usuario)

    conn.commit()

    cur.close()
    conn.close()

    print("Usuarios cargados")





    