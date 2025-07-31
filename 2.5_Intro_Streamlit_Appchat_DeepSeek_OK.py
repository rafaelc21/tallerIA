# Importacion de librerías
import os  # Para gestionar variables de entorno.
import streamlit as st  # Para construir la interfaz web interactiva.
from openai import OpenAI  # # Importa el cliente estandar de OpenAI.
from PIL import Image  # Para cargar y mostrar imágenes en Streamlit.
#import time

os.environ["DEEPSEEK_API_KEY"] = "sk-ebed09dc4b2242bebd1e21cd3be686d3"  # ¡Mantén tus claves seguras!

# Configuración de la Página - Titulo
st.set_page_config(page_title = "Chatbot usando la API de DeepSeek OpenAI", page_icon = "🤖")

with st.sidebar:
    st.title("Usando la API de DeepSeek")
    image = Image.open('2.5_logo.png')
    st.image(image, caption = 'DeepSeek')
    st.markdown(
        """
        Integrando DeepSeek con Streamlit.
    """
    )

msg_chatbot = """
        Soy un chatbot que está integrado a la API de DeepSeek: 

        ### Preguntas frecuentes
        
        - ¿Quién eres?
        - ¿Cómo funcionas?
        - ¿Cuál es tu capacidad o límite de conocimientos?
        - ¿Puedes ayudarme con mi tarea/trabajo/estudio?
        - ¿Tienes emociones o conciencia?
        - Lo que desees
"""

def clear_chat_history():
    st.session_state.messages = [{"role" : "assistant", "content": msg_chatbot}]

st.sidebar.button('Limpiar historial de chat', on_click = clear_chat_history)

def get_response(prompt):

    client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],  # Clave API de OpenAI.
    base_url="https://api.deepseek.com"  # URL base de la API. Por defecto https://api.openai.com/v1. Puedes cambiarla si estás utilizando otra solucion.
    )

    response = client.chat.completions.create(
    model="deepseek-chat",  # Nombre del modelo a utilizar como: "gpt-4-turbo" o "deepseek-chat"
    # Lista de mensajes del chat en formato [{role: "user", content: "Hola"}]
    messages=[  
        {"role": "system", "content": "Eres un asistente"},
        {"role": "user", "content": prompt}
    ],    
    stream=False,  # (True) la respuesta del modelo se envía en fragmentos (streaming) y (False) la respuesta del modelo como un bloque completo.
    #max_tokens=50,  # Límite máximo de tokens en la respuesta generada.
    temperature=0.7,  # Controla la aleatoriedad. Rango (0 a 2). Respuestas más deterministas (0.0 - 0.3). Respuestas muy aleatorias (1.3 - 2.0).
    )    
    return response.choices[0].message.content

#Si no existe la variable messages, se crea la variable y se muestra por defecto el mensaje de bienvenida al chatbot.
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content" : msg_chatbot}]

# Muestra todos los mensajes de la conversación
for message in st.session_state.messages:
    #time.sleep(1)  # Pausa de 1 segundo
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ingresa tu pregunta")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generar una nueva respuesta si el último mensaje es de un user
if st.session_state.messages[-1]["role"] == "user":
    with st.chat_message("assistant"):
        with st.spinner("Esperando respuesta, dame unos segundos."):
            response = get_response(prompt)
            placeholder = st.empty()
            placeholder.markdown(response)

    message = {"role" : "assistant", "content" : response}
    st.session_state.messages.append(message) #Agrega elemento a la caché de mensajes de chat.