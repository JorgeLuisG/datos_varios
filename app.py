import streamlit as st
from db import get_connection

try:
    conn = get_connection()

    cur = conn.cursor()
    cur.execute("SELECT NOW()")

    st.success("Conexión exitosa")
    st.write(cur.fetchone())

    cur.close()
    conn.close()

except Exception as e:
    st.error(str(e))