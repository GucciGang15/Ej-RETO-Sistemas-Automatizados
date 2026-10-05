import time
from serial import Serial
from unittest.mock import MagicMock
from view import crear_interfaz

MODO_SIMULACION = True  #CAMBIAR CUANDO CONSIGAMOS EL ARDUINO

puertoCom = "COM5" 

if not MODO_SIMULACION:
    #YA LO TENIAMOS ANTES
    arduino = Serial(port=puertoCom, baudrate=9600, timeout=1)
    time.sleep(2)
else:
    print("PROBANDO EN MODO SIMULACIÓN (Sin Arduino físico)")
    arduino = MagicMock()
    
    def simular_respuesta_arduino(comando_bytes):
        respuestas = {
            b'a': b'LED 1 encendido\n',
            b'A': b'LED 1 apagado\n',
            b'b': b'LED 2 encendido\n',
            b'B': b'LED 2 apagado\n',
            b'c': b'LED 3 encendido\n',
            b'C': b'LED 3 apagado\n',
        }
        arduino.readline.return_value = respuestas.get(comando_bytes, b'Valor no reconocido\n')

    arduino.write.side_effect = simular_respuesta_arduino

if __name__ == "__main__":
    app = crear_interfaz(arduino)
    app.mainloop()