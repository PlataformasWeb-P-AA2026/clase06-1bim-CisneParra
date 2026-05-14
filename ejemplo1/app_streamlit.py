import streamlit as st
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo
from configuracion import engine

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consultar docentes
saludos = session.query(Saludo).all()

# Mostrar con Streamlit
st.title("Presentación de todos los Saludos")

for saludo in saludos:
    mensaje = str(saludo).replace("-", " ").upper()
    st.write(mensaje)
    st.markdown("---")

st.markdown("---")
st.title("Presentación de todos los Saludos en Tabla")
lista = []

for s in saludos:
    diccionario = {
        "MENSAJE": s.mensaje.upper(),
        "TIPO": s.tipo.upper()
    }
    lista.append(diccionario)

st.dataframe(lista)
