# 🩺 Asistente de Seguros con IA (Voz + RAG)

Este proyecto es un prototipo funcional desarrollado para la **Hackathon de Healthcare**. Es un asistente virtual capaz de escuchar al paciente (Voz), transcribir su consulta y responder preguntas específicas sobre su cobertura médica basándose en un documento PDF real (Póliza) utilizando técnicas de **RAG (Retrieval-Augmented Generation)**.

## 🚀 Funcionalidades Clave

- **🗣️ Voz a Texto:** Transcripción de alta precisión usando **Whisper V3** (vía Groq).
- **🧠 Inteligencia Médica:** Razonamiento usando **Llama 3.3 70B** (vía Groq).
- **📚 RAG (Búsqueda en Póliza):** El asistente **lee** el PDF de la póliza en tiempo real para dar respuestas exactas sobre copagos y coberturas, evitando alucinaciones.
- **⚡ Ultra Rápido:** Arquitectura optimizada para baja latencia.

---

## 🛠️ Requisitos Previos

- **Python 3.8** o superior instalado.
- **Git** instalado.
- Una **API Key de Groq** (Gratuita). Puedes obtenerla en [console.groq.com](https://console.groq.com).

---

## 💻 Instalación y Ejecución Local

Sigue estos pasos para probar el proyecto en tu máquina.

### 1. Clonar el Repositorio

Abre tu terminal y ejecuta:

```bash
git clone [https://github.com/TU_USUARIO/TU_REPO.git](https://github.com/TU_USUARIO/TU_REPO.git)
cd TU_REPO
```

Luego ejecuta "streamlit run app.py" (sin comillas y listo. A usar).
