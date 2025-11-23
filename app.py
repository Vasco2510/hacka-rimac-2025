import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="Asistente de Seguros", page_icon="📄")
st.title("📄 Asistente de Póliza Inteligente")

api_key = os.getenv("GROQ_KEY")

client = Groq(api_key=api_key)

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# --- NUEVA FUNCIÓN: Cargar la Póliza ---
def cargar_contexto_poliza():
    try:
        with open("poliza.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: No se encontró el archivo poliza.txt"

# Cargamos la póliza en una variable
texto_poliza = cargar_contexto_poliza()

# --- Funciones Backend ---
def procesar_audio(audio_buffer):
    # (Esta función se mantiene igual que antes para Whisper)
    try:
        transcription = client.audio.transcriptions.create(
            file=("grabacion.wav", audio_buffer),
            model="whisper-large-v3",
            language="es",
            temperature=0.0
        )
        return transcription.text
    except Exception as e:
        st.error(f"Error audio: {e}")
        return None

def obtener_respuesta_ia(historial_chat):
    # --- CAMBIO CLAVE: Prompt Engineering ---
    # Aquí inyectamos la póliza dentro de las instrucciones
    prompt_sistema = f"""
    Eres un experto en seguros médicos. Tienes acceso a la siguiente PÓLIZA DE SEGURO:
    
    '''
    {texto_poliza}
    '''

    Instrucciones:
    1. Responde SOLO basándote en la póliza anterior.
    2. Si el usuario pregunta por costos, SIEMPRE genera un pequeño ejemplo matemático de cuánto pagaría.
    3. Sé empático pero claro con los números.
    4. Si la póliza no menciona algo, di "No encuentro esa información en tu póliza".
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": prompt_sistema},
            *historial_chat
        ],
        temperature=0.1, # Bajamos temperatura para que sea estricto con los datos
        max_tokens=400
    )
    return completion.choices[0].message.content

# --- Interfaz (Se mantiene igual) ---
for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])

audio_input = st.audio_input("Consulta sobre tu cobertura")

if audio_input is not None:
    with st.spinner("Consultando póliza..."):
        texto_usuario = procesar_audio(audio_input)
        
        if texto_usuario:
            with st.chat_message("user"):
                st.markdown(texto_usuario)
            st.session_state.mensajes.append({"role": "user", "content": texto_usuario})

            respuesta_ia = obtener_respuesta_ia(st.session_state.mensajes)
            
            with st.chat_message("assistant"):
                st.markdown(respuesta_ia)
            st.session_state.mensajes.append({"role": "assistant", "content": respuesta_ia})