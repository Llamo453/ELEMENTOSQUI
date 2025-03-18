import streamlit as st
import random

# Diccionario de elementos químicos
elementos = {
    "H": "Hidrógeno",
    "He": "Helio",
    "Li": "Litio",
    "Be": "Berilio",
    "B": "Boro",
    "C": "Carbono",
    "N": "Nitrógeno",
    "O": "Oxígeno",
    "F": "Flúor",
    "Ne": "Neón",
}

# Seleccionar un elemento al azar
simbolo, nombre = random.choice(list(elementos.items()))

# Configurar la interfaz de Streamlit
st.title("Juego de Elementos Químicos")
st.write("Adivina el nombre del elemento químico dado su símbolo")

st.subheader(f"Símbolo: {simbolo}")
respuesta = st.text_input("Escribe el nombre del elemento:")

if st.button("Verificar"):
    if respuesta.strip().capitalize() == nombre:
        st.success("¡Correcto!")
    else:
        st.error(f"Incorrecto. La respuesta correcta es {nombre}.")
