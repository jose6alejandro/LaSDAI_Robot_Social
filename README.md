# LaSDAI Robot Social 
Es un proyecto de bajo costo con el fin de desarrollar aplicaciones de interacción humano-robot

## Primera version LRS1 
Fue un primer acercamiento donde se realizó una investigación cuyo objetivo fue incorporar al robot social construido (denominado LRS1) como tutor en una actividad denominada “dictado” que pertenece al normal desarrollo de la asignatura, cuyos resultados obtenidos favorecen la incorporación de un robot social de bajo costo para motivar el aprendizaje en la asignatura.

## Segunda version LRS2
Es la versión actual que se basa en la primera cuyo objetivo es potenciar las investigaciones de interacción humano-robot.

- Modificaciones del lenguaje:
    - Ahora se utiliza Python por su flexibilidad y facilidad de adaptación.
- Modificaciones en la biblioteca pr1-ula
    - Modificado el programa para reproducir el audio, ahora se usa mpv
    - Agregado el nombre LRS2 para identificar el robot fisico 
    - Agregado el procedimiento hablarRobot2(int, char*, char*) para usar el gtts y mejorar la sincronización del movimiento de la boca
