import tkinter as tk
from funciones import controlBoton1, controlBoton2, controlBoton3

def crear_interfaz(arduino):
    # INTERFAZ GRÁFICA (TKINTER)
    ventana = tk.Tk()
    ventana.title("Control de LEDs")
    ventana.geometry("300x260")

    estadoLed1 = [False]
    estadoLed2 = [False]
    estadoLed3 = [False]

    #YA TENÍAMOS
    botonLed1 = tk.Button(
        ventana,
        text="Encender LED 1",
        font=("Arial", 12),
        width=16,
        command=lambda: controlBoton1(estadoLed1, botonLed1, lblmensaje, arduino)
    )
    botonLed1.place(x=70, y=30)

    #AGREGAMOS
    botonLed2 = tk.Button(
        ventana,
        text="Encender LED 2",
        font=("Arial", 12),
        width=16,
        command=lambda: controlBoton2(estadoLed2, botonLed2, lblmensaje, arduino)
    )
    botonLed2.place(x=70, y=80)

    botonLed3 = tk.Button(
        ventana,
        text="Encender LED 3",
        font=("Arial", 12),
        width=16,
        command=lambda: controlBoton3(estadoLed3, botonLed3, lblmensaje, arduino)
    )
    botonLed3.place(x=70, y=130)

    # LO QUE YA TENÍAMOS
    lblmensaje = tk.Label(ventana, text="-", font=("Arial", 10, "italic"))
    lblmensaje.place(x=40, y=190)

    return ventana