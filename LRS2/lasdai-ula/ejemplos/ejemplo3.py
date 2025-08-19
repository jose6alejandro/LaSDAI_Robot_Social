import cv2
import base64
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from ..modulo import pr1_ula as pr1
from ..modulo.pr1_ula  import pyaudio, wave, audioop
from ..modulo.pr1_ula import comando, load_dotenv

id = pr1.ula.conectarRobot(pr1.ROBOT.encode('utf-8'))

def capturar_img(nombre_archivo="foto.jpg"):

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        return None

    #print("Ajustando la exposición de la cámara...")
    for _ in range(10):
        cap.read()
        pr1.time.sleep(0.1)

    ret, frame = cap.read()
    cap.release()

    if ret:
        cv2.imwrite(nombre_archivo, frame)
       #print(f"✅ Foto guardada como {nombre_archivo}")
        return nombre_archivo
    else:
        print("❌ Error: No se pudo capturar la foto.")
        return None

def analizar_emocion(ruta_foto):

    if not ruta_foto:
        return "No hay foto para analizar."

    pr1.load_dotenv()
    google_api_key = pr1.os.getenv('GOOGLE_API_KEY')

    if not google_api_key:
        print("Error: La variable de entorno GOOGLE_API_KEY no está configurada.")
        return "Error de configuración."

    # Inicializa el modelo de Gemini (asegúrate de usar un modelo multimodal como gemini-1.5-flash)
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=google_api_key)

    # Lee y codifica la imagen en Base64
    with open(ruta_foto, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

    # Prepara el mensaje multimodal con la imagen y el texto
    mensaje = [
        HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": 
                    '''
                    <objetivo> 
                    A partir de la imagen proporcionada, su tarea es identificar la emoción principal del estudiante basándote únicamente en el conjunto de <emociones>.
                    </objetivo>

                    <contexto>
                        <emociones>
                        - sorpresa: Es una reacción breve e instantánea ante algo inesperado, que nos prepara para la siguiente emoción.
                        - feliz: Se asocia con la satisfacción y el bienestar, a menudo expresada a través de una sonrisa genuina.
                        - neutral: Es un estado sin emoción ni sesgo, un punto de equilibrio sin reacción fuerte.
                        - triste: Se asocia a sentimientos de dolor y puede ser provocada por la pérdida o desilusión.
                        - ira: Es una reacción de enojo ante amenazas o injusticias, que nos impulsa a confrontar.
                        - miedo: Se asocia con expresiones que nos prepara para responder y protegernos ante una amenaza. 
                        </emociones>

                        <caso_de_estudio>
                            manejo del estrés
                        </caso_de_estudio>  
                    </contexto>

                    <salida>
                    Tu respuesta debe ser **exclusivamente** en el siguiente formato:
                    'emoción': 'descripción concisa'.

                    por ejemplo:
                    feliz: El estudiante muestra una sonrisa genuina y relajada.
                    </salida>                 
                    '''
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}
                }
            ]
        )
    ]

    try:
        response = llm.invoke(mensaje)
        return response.content
    except Exception as e:
        return f"Error al interactuar con Gemini: {e}"

if __name__ == "__main__":
    nombre_de_foto = capturar_img()

    if nombre_de_foto:
        emocion_detectada = analizar_emocion(nombre_de_foto)
        emocion = emocion_detectada.split(':')[0]
        if emocion == "feliz":
            pr1.ula.enviarRobot(id, comando["expresarFeliz"])
        elif emocion == "triste":
            pr1.ula.enviarRobot(id, comando["expresarTriste"])
        
        print(f"{emocion_detectada}")
    
    pr1.ula.desconectarRobot(id);
        # Opcionalmente, puedes eliminar el archivo de la foto después de usarlo
        # os.remove(nombre_de_foto)
