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
    
  
    filas = len(map_data)
    colum = len(map_data[0])
    for row_idx in range(filas):
        for col_idx in range(colum):
            x1 = col_idx * cell_size
            y1 = row_idx * cell_size
            canvas.create_image(x1, y1, image=images[int(map_data[row_idx][col_idx])], anchor='nw')

def imprimir():
    
    for i in reversed(solucion):
        
        map_data = i

        
        draw_map(canvas, map_data)
        root.update()
        time.sleep(0.10)
    

def cerrar_ventana():
    root.destroy()

def cambiar_variable(valor):
    global tipo_busqueda
    tipo_busqueda = valor


def seleccionar_interfaz():
    respuesta = easygui.buttonbox("Seleccione la dificultad:", choices=["Principiante", "Amateur", "Experto"])
    if respuesta == "Principiante":
        cambiar_variable(True)
    else:
        cambiar_variable(False)



#Cargar Imagenes

img_HorseIA, img_HorsePlayer, Img_Uno, Img_Dos, Img_Tres, Img_Cuatro, Img_Cinco, Img_Seis, Img_Siete = Image.open('media/IA.png'), Image.open('media/player.png'), Image.open('media/1.png'), Image.open('media/2.png'), Image.open('media/3.png'), Image.open('media/4.png'), Image.open('media/5.png'), Image.open('media/6.png'), Image.open('media/7.png')  


img_HorseIA, img_HorsePlayer, Img_Uno, Img_Dos, Img_Tres, Img_Cuatro, Img_Cinco, Img_Seis, Img_Siete = img_HorseIA((cell_size - 2, cell_size - 2, )), img_HorsePlayer((cell_size - 2, cell_size - 2)), Img_Uno((cell_size -2, cell_size - 2)), Img_Dos((cell_size -2, cell_size - 2)), Img_Tres((cell_size -2, cell_size - 2)), Img_Cuatro((cell_size -2, cell_size - 2)), Img_Cinco((cell_size -2, cell_size - 2)), Img_Seis((cell_size -2, cell_size - 2)), Img_Siete((cell_size -2, cell_size - 2))

#Formate compatible con tkinter

img_HorseIA, img_HorsePlayer = ImageTk.PhotoImage(img_HorseIA), ImageTk.PhotoImage(img_HorsePlayer), ImageTk.PhotoImage(Img_Uno), ImageTk.PhotoImage(Img_Dos), ImageTk.PhotoImage(Img_Tres), ImageTk.PhotoImage(Img_Cuatro), ImageTk.PhotoImage(Img_Cinco), ImageTk.PhotoImage(Img_Seis), ImageTk.PhotoImage(Img_Siete)    

solucion = []