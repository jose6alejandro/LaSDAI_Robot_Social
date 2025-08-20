# LaSDAI Robot Social 2

## Configuración
Para la configuración del robot instale los paquetes necesarios:

```
sudo apt install python3.9-dev mpv portaudio19-dev alsa-utils pulseaudio libgl1-mesa-glx
pip install gtts vosk PyAudio wave 
pip install langchain langchain_google_genai 
pip install python-dotenv
pip install opencv-python
```

## Ejecución
Si la configuración de los paquetes fue exitosa puede empezar.
Pruebe ejecutando el primer programa:

```
python -m lasdai_ula.ejemplos.ejemplo1
```

## Ejemplos
- Ejemplo 1: hola mundo
- Ejemplo 2: conversación usando LLM
- Ejemplo 3: reconocimiento de emoción
