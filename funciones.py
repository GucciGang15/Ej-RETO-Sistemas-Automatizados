#LO QUE YA TENÍAMOS
def leerMensajeArduino(arduino):
    mensajeLed = arduino.readline().decode().strip()
    print("Respuesta recibida del Arduino:", mensajeLed)
    return mensajeLed


#LO QUE YA TENÍAMOS
def controlBoton1(estadoLed1, botonLed1, lblmensaje, arduino):
    if estadoLed1[0]:
        estadoLed1[0] = False
        botonLed1.config(text="Encender LED 1")
        arduino.write(b'A')  # Comando para apagar LED 1
    else:
        estadoLed1[0] = True
        botonLed1.config(text="Apagar LED 1")
        arduino.write(b'a')  # Comando para encender LED 1

    lblmensaje.config(text=leerMensajeArduino(arduino))


#AGREGAMOS
def controlBoton2(estadoLed2, botonLed2, lblmensaje, arduino):
    if estadoLed2[0]:
        estadoLed2[0] = False
        botonLed2.config(text="Encender LED 2")
        arduino.write(b'B')  # Comando para apagar LED 2
    else:
        estadoLed2[0] = True
        botonLed2.config(text="Apagar LED 2")
        arduino.write(b'b')  # Comando para encender LED 2

    lblmensaje.config(text=leerMensajeArduino(arduino))


#AGREGAMOS
def controlBoton3(estadoLed3, botonLed3, lblmensaje, arduino):
    if estadoLed3[0]:
        estadoLed3[0] = False
        botonLed3.config(text="Encender LED 3")
        arduino.write(b'C')  # Comando para apagar LED 3
    else:
        estadoLed3[0] = True
        botonLed3.config(text="Apagar LED 3")
        arduino.write(b'c')  # Comando para encender LED 3

    lblmensaje.config(text=leerMensajeArduino(arduino))