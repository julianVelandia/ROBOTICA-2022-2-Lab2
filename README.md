# LABORATORIO 2.
## ROBOTICA 2022-2
### Julian Camilo Velandia & Sebastian Cubides Toscano.
***
### 1. Conexión de ROS con MATLAB:

Se siguío el procedimiento descrito en la guía [1], creando 3 scripts, uno para darle movimiento a la tortuga, otro para suscribirse al tópico de la pose de la tortuga y el último para enviar los valores asociados a la pose de la tortuga. 

Los scripts de MATLAB se encuentran nombrados según su función.

En la siguiente imagen se observan los resultados.

![SSTurtleMatlab](SSTurtleMatlab.png)
***
### 2. Conexión de ROS con PYTHON:

Se siguío el procedimiento descrito en la guía [1] para sincronizar ROS con PYTHON, posteriormente se uso el código encontrado en [3] para la lectura de eventos y por último se programaron los movimientos establecidos a las teclas a, s, d, w, r y espacio. La asignación de los movimiento se hizo de la siguiente forma:

* 'a' -> movimiento en x negativo.
* 's' -> movimiento en y negativo.
* 'd' -> movimiento en x positivo.
* 'w' -> movimiento en y positivo.
* 'r' -> se retorna a la posición de inicio.
* '_' -> se realiza un giro de 180 grados.

El codigo construido para este ejercicio se encuentra adjunto como myTeleopKey.py.

Adicionalmente se muestra el funcionamiento en el siguiente video.

[![Alt text](https://img.youtube.com/vi/Y9_tDsX4t0E/0.jpg)](https://youtu.be/Y9_tDsX4t0E)

***

### 3. Referencias:
1. Laboratorio 2 - Robótica de Desarrollo, Intro a ROS. 2022-2. Universidad Nacional de Colombia.
2. ROS.org. Rotating Left/Right. http://wiki.ros.org/turtlesim/Tutorials/Rotating%20Left%20and%20Right  
3. Python for Fun. Get Key Press in Python. http://python4fun.blogspot.com/2008/06/get-key-press-in-python.html