import io
import os
import ctypes
import tempfile
import pyaudio
import wave
import audioop
import time
import json

from dotenv import load_dotenv

from gtts import gTTS

from vosk import Model, KaldiRecognizer, SetLogLevel

# Permiso para el puerto del robot
RUTA_PUERTO = "/dev"
os.system(f"sudo chmod -R 777 {RUTA_PUERTO}")

# Modelo de reconocimiento de voz
MODEL = "vosk-model-small-es-0.42"

# Parámetros de grabación
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
SILENCE_THRESHOLD = 1000
MAX_SILENCE_SECONDS = 2

# Configuraciones del robot
ROBOT = "LRS2"

# voces: alentador, empatico, analitico, calmado

comando = {
    "expresarNormal": 4, 
    "cerrarOjos": 59, 
    "abrirOjos": 64,
    "cerrarIzquierdo": 5, 
    "abrirIzquierdo": 6, 
    "cerrarDerecho": 7,
    "abrirDerecho": 8, 
    "comenzarHabla": 9, 
    "terminarHabla": 44,
    "moverIzquierda": 45, 
    "moverCentro": 46, 
    "moverDerecha": 47,
    "moverArriba": 48, 
    "mover_cuelloCe": 49, 
    "moverAbajo": 54,
    "expresarFeliz": 55, 
    "expresarTriste": 56, 
    "habilitarEntradas": 57,
    "deshabilitarEntradas": 58
}

try:
    ula = ctypes.CDLL('./lasdai-ula/modulo/pr1-ula.so')
except OSError as e:
    print(f"Error al cargar la biblioteca: {e}")

def respuestaRobot(pr1, id, personalidad, texto):
    # Generar el audio directamente en un buffer de memoria
    tts = gTTS(text=texto, lang='es', tld='co.ve')
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as temp_file:
        temp_file.write(mp3_fp.getvalue())
        temp_file.flush() # Asegura que todos los datos se han escrito

        ula.hablarRobot2(id, personalidad.encode('utf-8'), temp_file.name.encode('utf-8'))
