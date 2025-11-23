import os
from groq import Groq

# Usamos la misma llave de Groq para ambas cosas
client = Groq(api_key=GROQ_KEY)

def transcribir_audio(ruta_archivo):
    with open(ruta_archivo, "rb") as file:
        # Paso 1: Voz a Texto
        transcription = client.audio.transcriptions.create(
            file=(ruta_archivo, file.read()),
            model="whisper-large-v3",
            language="es"
        )
    return transcription.text

def obtener_respuesta_ia(texto_paciente):
    # Definimos el rol del sistema (System Prompt)
    prompt_sistema = """
    Eres un asistente virtual útil para triaje médico primario. 
    Responde de forma empática, breve y profesional. 
    No des diagnósticos definitivos, solo sugerencias y pasos a seguir. En maximo 200 palabras
    """

    # Paso 2: Texto a Inteligencia
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": texto_paciente}
        ],
        temperature=0.5, # Un valor bajo para ser más preciso y menos "creativo"
        max_tokens=150   # Limitamos la longitud para que no suelte discursos largos
    )
    
    return completion.choices[0].message.content

if __name__ == "__main__":
    audio_prueba = "audiosPrueba/a-1-t.mp3"
    
    print(f"1. Escuchando archivo: {audio_prueba} ...")
    texto_transcrito = transcribir_audio(audio_prueba)
    print(f"   -> Paciente dijo: '{texto_transcrito}'\n")
    
    print("2. Consultando al Asistente Médico...")
    respuesta_medica = obtener_respuesta_ia(texto_transcrito)
    
    print("\n--- Respuesta del Asistente ---")
    print(respuesta_medica)