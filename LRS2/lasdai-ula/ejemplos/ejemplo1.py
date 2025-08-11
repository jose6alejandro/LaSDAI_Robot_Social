# En hola_mundo.py
from ..modulo import pr1_ula as pr1
from ..modulo.pr1_ula import comando

def main():
    
    id =  pr1.ula.conectarRobot(pr1.ROBOT.encode('utf-8'));

    pr1.respuestaRobot(pr1, id, "alentador", "Hola mundo!");
    pr1.ula.enviarRobot(id, comando["expresarFeliz"]);

    pr1.ula.desconectarRobot(id);

if __name__ == "__main__":
  main()
