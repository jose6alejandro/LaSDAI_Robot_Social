from ..modulo import pr1_ula as pr1
from ..modulo.pr1_ula  import pyaudio, wave, audioop, time, json, io
from ..modulo.pr1_ula import Model, KaldiRecognizer, SetLogLevel
from ..modulo.pr1_ula import comando, load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, SystemMessage

# Configurar API Key de Gemini

pr1.load_dotenv()

pr1.os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# Iniciar robot
id = pr1.ula.conectarRobot(pr1.ROBOT.encode('utf-8'))

# Iniciar stream
p = pyaudio.PyAudio()
stream = p.open(format=pr1.FORMAT, channels=pr1.CHANNELS, rate=pr1.RATE, input=True, frames_per_buffer=pr1.CHUNK)

#  Iniciar modelo vosk
SetLogLevel(-1) # Oculta logs
model = Model(pr1.MODEL)
rec = KaldiRecognizer(model, pr1.RATE)

pr1.respuestaRobot(pr1, id, "analitico", "Hola, en qué puedo ayudarte")
#print("Escuchando...")

# 💬 Historial de la conversación
chat_history = []

# Bucle de grabación y transcripción en tiempo real
while True:
    frames = []
    texto_transcrito = ""
    silence_start = None

    while True:
        data = stream.read(pr1.CHUNK)
        frames.append(data)
        rms = audioop.rms(data, 2)

        # Transcribir en tiempo real
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            texto_transcrito += result.get("text", "") + " "
            # print("Parcial:", result.get("text", ""))

        # Detección de silencio
        if rms < pr1.SILENCE_THRESHOLD:
            if silence_start is None:
                silence_start = time.time()
            elif time.time() - silence_start > pr1.MAX_SILENCE_SECONDS:
                print("🛑 Silencio detectado. Procesando audio.")
                break
        else:
            silence_start = None

    # 📝 Obtener resultado final de la transcripción del segmento
    final = json.loads(rec.FinalResult())
    texto_transcrito += final.get("text", "")
    user_message = texto_transcrito.strip()

   ## print("🎤 Texto reconocido:", user_message)

    # 🛑 Condición de finalización
    if any(keyword in user_message.lower() for keyword in ["terminar", "adiós", "cancelar"]):
        pr1.respuestaRobot(pr1, id, "alentador", "Claro, adiós. ¡Que tengas un excelente día!")
        break

    # 🤖 Si el texto no está vacío, procesar con Gemini
    if user_message:
        # Añadir mensaje del usuario al historial
        chat_history.append(HumanMessage(content=user_message))

        # Prompt para Gemini (considerando el historial)
        prompt = [SystemMessage(content="Responde brevemente a la solicitud del usuario. Considera que tu respuesta será verbal, así que no añadas caracteres especiales. Si no hay texto, pidele que repita nuevamente.")] + chat_history
        
        try:
            respuesta = llm.invoke(prompt)
            # Añadir respuesta del modelo al historial
            chat_history.append(respuesta)
            pr1.respuestaRobot(pr1, id, "alentador", respuesta.content)
            print("LRS2 responde:", respuesta.content)
        except Exception as e:
            print(f"Ocurrió un error con LRS2: {e}")
            pr1.respuestaRobot(pr1, id, "alentador", "¿Podrías repetirlo?")

# Finalizar la conexión
stream.stop_stream()
stream.close()
p.terminate()
pr1.ula.desconectarRobot(id)
