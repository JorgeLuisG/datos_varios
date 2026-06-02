import streamlit as st
import streamlit_authenticator as stauth

from crear_tabla import crear_tabla_usuarios
from cargar_usuarios import cargar_usuarios_iniciales

crear_tabla_usuarios()
cargar_usuarios_iniciales()

from auth import (
    obtener_credenciales,
    obtener_rol
)

credentials = obtener_credenciales()