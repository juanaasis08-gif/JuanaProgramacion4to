import tkinter as tk
import random

# Crear la ventana principal

ventana = tk.Tk()

ventana.title("MEMOTEST")
ventana.geometry("500x550")
ventana.configure(bg="#F8DDEB")
# Crear las cartas del juego

cartas = [1, 2, 3, 4, 5, 6, 7, 8] * 2

random.shuffle(cartas)
# Variables del juego

primera = None
segunda = None

bloqueado = False
encontradas = 0

botones = []
# Función para elegir una carta

def elegir(posicion):

    global primera, segunda, bloqueado, encontradas

    if bloqueado:
        return

    boton = botones[posicion]

    if boton["text"] != "?":
        return

    boton.config(text=str(cartas[posicion]))

    if primera is None:
        primera = posicion

    else:
        segunda = posicion
        comprobar()
        # Comprobar si las cartas son iguales

def comprobar():

    global primera, segunda, bloqueado, encontradas

    if cartas[primera] == cartas[segunda]:

        encontradas += 1

        primera = None
        segunda = None

        mensaje.config(text="¡Encontraste un par!")

        if encontradas == 8:
            mensaje.config(text="¡FELICITACIONES! GANASTE")

    else:

        bloqueado = True

        mensaje.config(text="No son iguales. ¡Intentá otra vez!")

        ventana.after(1000, tapar)
        # Volver a tapar las cartas

def tapar():

    global primera, segunda, bloqueado

    botones[primera].config(text="?")
    botones[segunda].config(text="?")

    primera = None
    segunda = None

    bloqueado = False

    mensaje.config(text="Buscá los pares")
    # Crear los botones

for i in range(16):

    boton = tk.Button(
        ventana,
        text="?",
        width=8,
        height=4,
        font=("Arial", 16, "bold"),
        bg="white",
        fg="#C65A91",
        command=lambda i=i: elegir(i)
    )

    boton.grid(
        row=i//4 + 1,
        column=i%4,
        padx=8,
        pady=8
    )

    botones.append(boton)
    # Crear el título

titulo = tk.Label(
    ventana,
    text="MEMOTEST",
    font=("Arial", 24, "bold"),
    bg="#F8DDEB",
    fg="#C65A91"
)

titulo.grid(row=0, column=0, columnspan=4, pady=15)


# Crear el mensaje

mensaje = tk.Label(
    ventana,
    text="¡Encontrá los 8 pares!",
    font=("Arial", 14),
    bg="#F8DDEB",
    fg="#C65A91"
)

mensaje.grid(row=5, column=0, columnspan=4, pady=15)
# Mantener abierta la ventana

ventana.mainloop()
