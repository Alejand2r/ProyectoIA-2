import tkinter as tk
from tkinter import filedialog
import time
from PIL import Image, ImageTk
import easygui as eg

WINDOW_SIZE = 700

with open("input.txt", "r") as read_file:
    matriz = read_file.readlines()
    estado_inicial = ""
    for row in matriz:
        for cell in row.split():
            if cell == '0':
                estado_inicial += '0'
            elif int(cell) in range(1, 8):
                estado_inicial += cell
            elif cell == '8':
                estado_inicial += 'b'
            elif cell == '9':
                estado_inicial += 'n'
            else:
                "error"
root = tk.Tk()
root.title("Smart Horses")
root.resizable(False, False)

canvas = tk.Canvas(root, width=WINDOW_SIZE - 50, height=WINDOW_SIZE)
canvas.pack()

cell_size = (WINDOW_SIZE - 50) // 8

img_HorseIA, img_HorsePlayer, Img_Cero, Img_Uno, Img_Dos, Img_Tres, Img_Cuatro, Img_Cinco, Img_Seis, Img_Siete = Image.open(
    'media/IA.png'), Image.open('media/player.png'), Image.open('media/0.png'), Image.open('media/1.png'), Image.open(
    'media/2.png'), Image.open(
    'media/3.png'), Image.open('media/4.png'), Image.open('media/5.png'), Image.open('media/6.png'), Image.open(
    'media/7.png')

img_HorseIA, img_HorsePlayer, Img_Cero, Img_Uno, Img_Dos, Img_Tres, Img_Cuatro, Img_Cinco, Img_Seis, Img_Siete = img_HorseIA.resize(
    (cell_size - 2, cell_size - 2)), img_HorsePlayer.resize((cell_size - 2, cell_size - 2)), Img_Cero.resize(
    (cell_size - 2, cell_size - 2)), Img_Uno.resize(
    (cell_size - 2, cell_size - 2)), Img_Dos.resize((cell_size - 2, cell_size - 2)), Img_Tres.resize(
    (cell_size - 2, cell_size - 2)), Img_Cuatro.resize((cell_size - 2, cell_size - 2)), Img_Cinco.resize(
    (cell_size - 2, cell_size - 2)), Img_Seis.resize((cell_size - 2, cell_size - 2)), Img_Siete.resize(
    (cell_size - 2, cell_size - 2))

img_HorseIA, img_HorsePlayer, Img_Cero, Img_Uno, Img_Dos, Img_Tres, Img_Cuatro, Img_Cinco, Img_Seis, Img_Siete = ImageTk.PhotoImage(
    img_HorseIA), ImageTk.PhotoImage(img_HorsePlayer), ImageTk.PhotoImage(Img_Cero), ImageTk.PhotoImage(
    Img_Uno), ImageTk.PhotoImage(
    Img_Dos), ImageTk.PhotoImage(Img_Tres), ImageTk.PhotoImage(Img_Cuatro), ImageTk.PhotoImage(
    Img_Cinco), ImageTk.PhotoImage(Img_Seis), ImageTk.PhotoImage(
    Img_Siete)

#funcion a ejecutar cuando el usuario hace una jugada
def new_play():
    pass

#funcion que dibuja el tablero apartir de un estado
def draw_map(estado: str):
    images = {
        "0": Img_Cero,
        "1": Img_Uno,
        "2": Img_Dos,
        "3": Img_Tres,
        "4": Img_Cuatro,
        "5": Img_Cinco,
        "6": Img_Seis,
        "7": Img_Siete,
        "b": img_HorseIA,
        "n": img_HorsePlayer
    }
    #Busca las posiciones en la que el usuario
    player_pos = estado.index("n")
    player_pos_x, player_pos_y = player_pos // 8, player_pos % 8
    posible_next_plax_pos = []
    if player_pos_x > 1:
        if player_pos_y > 0:
            posible_next_plax_pos.append(player_pos - 17)
        if player_pos_y < 7:
            posible_next_plax_pos.append(player_pos - 15)
    if player_pos_y < 6:
        if player_pos_x > 0:
            posible_next_plax_pos.append(player_pos - 6)
        if player_pos_x < 7:
            posible_next_plax_pos.append(player_pos + 10)
    if player_pos_x < 6:
        if player_pos_y > 0:
            posible_next_plax_pos.append(player_pos + 15)
        if player_pos_y < 7:
            posible_next_plax_pos.append(player_pos + 17)
    if player_pos_y > 1:
        if player_pos_x > 0:
            posible_next_plax_pos.append(player_pos - 10)
        if player_pos_x < 7:
            posible_next_plax_pos.append(player_pos + 6)

    for row_idx in range(8):
        for col_idx in range(8): #se pone un boton en caso de ser una jugada posible, caso contrario una imagen
            if (row_idx * 8 + col_idx) in posible_next_plax_pos:
                x = col_idx * cell_size
                y = row_idx * cell_size + 50
                button = tk.Button(root, image=images.get(estado[row_idx * 8 + col_idx]), command=new_play)
                button.pack(pady=20)
                button.place(x=x, y=y)
            else:
                x = (col_idx + 1 / 2) * cell_size
                y = (row_idx + 1 / 2) * cell_size + 50
                canvas.create_image(x, y, image=images.get(estado[row_idx * 8 + col_idx]))


draw_map(estado_inicial)
root.mainloop()


# def draw_map(canvas, map_data):
#     global images
#
#     filas = len(map_data)
#     colum = len(map_data[0])
#     for row_idx in range(filas):
#         for col_idx in range(colum):
#             x1 = col_idx * cell_size
#             y1 = row_idx * cell_size
#             canvas.create_image(x1, y1, image=images[int(map_data[row_idx][col_idx])], anchor='nw')
#
#
# def imprimir():
#     for i in reversed(solucion):
#         map_data = i
#
#         draw_map(canvas, map_data)
#         root.update()
#         time.sleep(0.10)
#
#
# def cerrar_ventana():
#     root.destroy()
#
#
# def cambiar_variable(valor):
#     global tipo_busqueda
#     tipo_busqueda = valor
#
#
# def seleccionar_interfaz():
#     respuesta = easygui.buttonbox("Seleccione la dificultad:", choices=["Principiante", "Amateur", "Experto"])
#     if respuesta == "Principiante":
#         cambiar_variable(True)
#     else:
#         cambiar_variable(False)
#
#
# # Cargar Imagenes
#
# img_HorseIA, img_HorsePlayer, Img_Uno, Img_Dos, Img_Tres, Img_Cuatro, Img_Cinco, Img_Seis, Img_Siete = Image.open(
#     'media/IA.png'), Image.open('media/player.png'), Image.open('media/1.png'), Image.open('media/2.png'), Image.open(
#     'media/3.png'), Image.open('media/4.png'), Image.open('media/5.png'), Image.open('media/6.png'), Image.open(
#     'media/7.png')
#
# img_HorseIA, img_HorsePlayer, Img_Uno, Img_Dos, Img_Tres, Img_Cuatro, Img_Cinco, Img_Seis, Img_Siete = img_HorseIA(
#     (cell_size - 2, cell_size - 2,)), img_HorsePlayer((cell_size - 2, cell_size - 2)), Img_Uno(
#     (cell_size - 2, cell_size - 2)), Img_Dos((cell_size - 2, cell_size - 2)), Img_Tres(
#     (cell_size - 2, cell_size - 2)), Img_Cuatro((cell_size - 2, cell_size - 2)), Img_Cinco(
#     (cell_size - 2, cell_size - 2)), Img_Seis((cell_size - 2, cell_size - 2)), Img_Siete((cell_size - 2, cell_size - 2))
#
# # Formate compatible con tkinter
#
# img_HorseIA, img_HorsePlayer, Img_Uno, Img_Dos, Img_Tres, Img_Cuatro, Img_Cinco, Img_Seis, Img_Siete = ImageTk.PhotoImage(
#     img_HorseIA), ImageTk.PhotoImage(img_HorsePlayer), ImageTk.PhotoImage(Img_Uno), ImageTk.PhotoImage(
#     Img_Dos), ImageTk.PhotoImage(Img_Tres), ImageTk.PhotoImage(Img_Cuatro), ImageTk.PhotoImage(
#     Img_Cinco), ImageTk.PhotoImage(Img_Seis), ImageTk.PhotoImage(Img_Siete)
#
# solucion = []