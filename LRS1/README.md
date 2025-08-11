# LRS2
**LaSDAI Robot Social 2 (LRS2)**

## Requisitos
- *espeak* y *mplayer*
```sh
$ sudo apt install espeak mplayer
```
#### Modificar la linea del archivo **Makefile** de acuerdo al sistema operativo:

- Linux 32bits:
```sh
 biblioteca = 32bits
```
-   Linux 64bits:
```sh
 biblioteca = 64bits
```
-   Raspberry:
```sh
 biblioteca = Raspberry
```
## Compilación y ejecución
- Ejemplo del programa hola mundo:
```sh
$ make ejemplo1
$ sudo ./ejemplo1
```
LISTO. El robot debe decir **Hola Mundo** 

## Ejemplos
1. El robot reproduce "Hola mundo"
2. Recibe información de botones 
3. Recibe información de otro computador
4. Envía información hacia el robot desde otro computador
5. Presentación del LRS2
6. Voces del robot
