# Ej-RETO-Sistemas-Automatizados
Ejercicio Reto Sistemas Automatizados

pip install pyserial

Ampliar la práctica de clase para controlar 3 LEDs de forma independiente desde Python, usando dos interfaces: el monitor serial (consola arduino) y una ventana en Tkinter.
Punto de partida: los archivos vistos en clase controlLedArduino.ino (sketch de Arduino) y controlLedGUI.py (interfaz en Tkinter), que encienden y apagan un solo LED en el pin 13 enviando 1 y 0 por el puerto serial a 9600 baudios.

Instrucciones
1. Circuito: agregar 2 LEDs al circuito original (3 en total), cada uno con su resistencia de 330 Ω y en un pin digital distinto (ejemplo: pines 11, 12 y 13).
2. Protocolo de comandos: definir un comando distinto para encender y apagar cada LED. Ejemplo:

LED    Encender       Apagar

LED 1     a              A
LED 2     b              B
LED 3     c              C

3. Código Arduino: modificar controlLedArduino.ino para que lea cada comando, encienda o apague el LED correcto y responda por serial con un mensaje de confirmación (ejemplo: LED 2 encendido). Conservar el mensaje "Valor no reconocido" para comandos inválidos.
4. Control por Monitor Serial: probar los 3 LEDs escribiendo los comandos en el Monitor Serial del IDE de Arduino (9600 baudios) y verificar que aparezcan los mensajes de confirmación. Cerrar el Monitor Serial antes de ejecutar Python, porque el puerto no puede usarse en dos programas a la vez.
5. Control con Tkinter: actualizar controlLedGUI.py para tener 3 botones, uno por LED. Cada botón alterna entre "Encender" y "Apagar" y lleva su propio estado (no una sola variable para todos).
6. Mensaje del Arduino: la ventana debe mostrar en una etiqueta la confirmación que devuelve el Arduino después de cada acción.
7. Prueba: verificar que los 3 LEDs funcionen por separado y en cualquier combinación desde ambas interfaces.