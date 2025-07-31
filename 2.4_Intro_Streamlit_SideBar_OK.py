import streamlit as st

st.set_page_config(page_title = "Uso de sidebar", page_icon = "📊")

st.sidebar.header("Menú de opciones")

nombre = st.sidebar.text_input("🔹 Ingresa tu nombre:")

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'Elige una opción', ['Email', 'Home phone', 'Mobile phone']
)

# Add radio
add_radio = st.sidebar.radio(
    "Elige tu color favorito", ["Verde", "Rojo", "Amarillo"],
    index = 0
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Selecciona un rango', 0, 100, (25, 75)
)
boton = st.sidebar.button("🔹 Presiona para confirmar")

st.title("Mostrando valores")

st.write("---")
st.write(f"👋 ¡Hola, {nombre}!")
st.write('Seleccionaste (Lista): ', add_selectbox)
st.write("Seleccionaste (Radio):", add_radio)
st.write('Seleccionaste (Slider) : ', add_slider)

# Mensaje al presionar el botón
if boton:
    st.success("✅ ¡Botón presionado con éxito!")