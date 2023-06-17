import tkinter as tk
from tkinter import filedialog
import time
from PIL import Image, ImageTk
import easygui as eg 

WINDOW_SIZE = 700

with open("input.txt", "r") as read_file:
    matriz = read_file.readlines()
    traductor = {"0": "l", "1": "m", "2": "g", "3": "f", "4": "c", "5": "s", "6": "e"}
    estado_inicial = ""
    for row in matriz:
        for cell in row.split():
            estado_inicial += traductor.get(cell)

root = tk.Tk()
root.title("Smart Horses")
root.resizable(False,False)

canvas = tk.Canvas(root, width=WINDOW_SIZE - 50, height=WINDOW_SIZE)
canvas.pack()

cell_size = (WINDOW_SIZE - 50) // 10

def draw_map(canvas, map_data):
    global images
    
    # Dibujar cada celda en el canvas con la imagen correspondiente
    filas = len(map_data)
    colum = len(map_data[0])
    for row_idx in range(filas):
        for col_idx in range(colum):
            x1 = col_idx * cell_size
            y1 = row_idx * cell_size
            canvas.create_image(x1, y1, image=images[int(map_data[row_idx][col_idx])], anchor='nw')

def imprimir():
    # Actualizar el ciclo for para que recorra la lista de soluciones
    for i in reversed(solucion):
        # Definir el mapa que se desea mostrar
        map_data = i

        # Dibujar el mapa en el canvas
        draw_map(canvas, map_data)
        root.update()
        time.sleep(0.10)
    
# Actualizar los valores de las etiquetas
def actualizarValores(expand, prof, tiem, cost):
    etiqueta_costo.config(text='Costo de la solución: ' + str(cost))

def cerrar_ventana():
    root.destroy()

def cambiar_variable(valor):
    global tipo_busqueda
    tipo_busqueda = valor

# Función que muestra la interfaz flotante para seleccionar entre busqueda informada o no informada
def mostrar_interfaz():
    respuesta = easygui.buttonbox("Seleccione la dificultad:", choices=["Principiante", "Amateur", "Experto"])
    if respuesta == "Principiante":
        cambiar_variable(True)
    else:
        cambiar_variable(False)



#Cargar Imagenes

img_HorseIA = Image.open('media/IA.png') #caballo blanco de la IA
img_HorsePlayer= Image.open('media/player.png') #caballo negro del jugador 

img_HorseIA, img_HorsePlayer = img_HorseIA((cell_size - 2, cell_size - 2, )), img_HorsePlayer((cell_size - 2, cell_size - 2))

#Formate compatible con tkinter

img_HorseIA, img_HorsePlayer = ImageTk.PhotoImage(img_HorseIA), ImageTk.PhotoImage(img_HorsePlayer)    

solucion = []