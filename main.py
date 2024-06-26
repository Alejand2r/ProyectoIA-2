import random
import tkinter as tk
from functools import partial

from PIL import Image, ImageTk

from minimax import minimax
from node import Nodo

WINDOW_SIZE = 700
Profundidad = None
with open("input.txt", "r") as read_file:
    matriz = read_file.readlines()
    estado_inicial_ing = ""
    for row in matriz:
        for cell in row.split():
            estado_inicial_ing += cell
root = tk.Tk()
root.title("Smart Horses")
root.resizable(False, False)

canvas = tk.Canvas(root, width=WINDOW_SIZE - 55, height=WINDOW_SIZE - 5)
canvas.pack()

cell_size = (WINDOW_SIZE - 50) // 8
nodo = None
img_HorseIA, img_HorsePlayer, Img_Cero, Img_Uno, Img_Dos, Img_Tres, Img_Cuatro, Img_Cinco, Img_Seis, Img_Siete = \
    Image.open('media/IA.png'), Image.open('media/player.png'), Image.open('media/0.png'), Image.open('media/1.png'), \
        Image.open('media/2.png'), Image.open('media/3.png'), Image.open('media/4.png'), Image.open('media/5.png'), \
        Image.open('media/6.png'), Image.open('media/7.png')

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


def new_play(Pos):
    global nodo
    nuevo_nodo = nodo.make_player_move(Pos)
    nodo = nuevo_nodo
    draw_map()
    label_estado.config(text=f"Jugador: {nodo.player_points}   Maquina: {nodo.machine_points}")
    utility, siguiente_nodo = minimax(nodo, profundidad=Profundidad)
    nodo = siguiente_nodo
    canvas.after(400, draw_map)
    label_estado.config(text=f"Jugador: {nodo.player_points}   Maquina: {nodo.machine_points}")


button_opt = []


# funcion que dibuja el tablero apartir de un estado
def draw_map():
    global button_opt
    global nodo
    if len(button_opt) > 0:
        for button in button_opt:
            button.place_forget()
        button_opt = []
    if nodo.game_end:
        if nodo.machine_points == nodo.player_points:
            message = f"Hubo un empate con {nodo.player_points} puntos"
        elif nodo.machine_points < nodo.player_points:
            message = f"Felicidades ganaste con {nodo.player_points} puntos"
        else:
            message = f"Has perdido {nodo.player_points} puntos a {nodo.machine_points}"
        label_estado.config(text=message)
        button_reinicio.pack
        button_reinicio.pack(pady=20)
        button_reinicio.place(x=500, y=15)
    images = {
        "0": Img_Cero,
        "1": Img_Uno,
        "2": Img_Dos,
        "3": Img_Tres,
        "4": Img_Cuatro,
        "5": Img_Cinco,
        "6": Img_Seis,
        "7": Img_Siete,
        "8": img_HorseIA,
        "9": img_HorsePlayer
    }
    for row_idx in range(8):
        for col_idx in range(8):  # se pone un boton en caso de ser una jugada posible, caso contrario una imagen
            if not nodo.game_end and nodo.player_move and (row_idx * 8 + col_idx) in nodo.get_posible_next_play_player():
                x = col_idx * cell_size
                y = row_idx * cell_size + 50
                button = tk.Button(root, image=images.get(nodo.state[row_idx * 8 + col_idx]),
                                   command=partial(new_play, row_idx * 8 + col_idx))
                button_opt.append(button)
                button.pack(pady=20)
                button.place(x=x, y=y)
            else:
                x = (col_idx + 1 / 2) * cell_size
                y = (row_idx + 1 / 2) * cell_size + 50
                canvas.create_image(x, y, image=images.get(nodo.state[row_idx * 8 + col_idx]))


def iniciarJuego(dificultad):
    global Profundidad
    global nodo
    button_dif_principiante.place_forget()
    button_dif_amateur.place_forget()
    button_dif_experto.place_forget()
    label_estado.place_forget()
    label_estado.place(x=200, y=15)
    label_estado.config(text=f"Jugador: {nodo.player_points}   Maquina: {nodo.machine_points}")
    if dificultad == "Principiante":
        profundidad = 2
    elif dificultad == "Amateur":
        profundidad = 4
    else:
        profundidad = 6
    nodo.set_max_deep(profundidad)
    utility, siguiente_nodo = minimax(nodo, profundidad=profundidad)
    Profundidad = profundidad
    nodo = siguiente_nodo
    label_estado.config(text=f"Jugador: {nodo.player_points}   Maquina: {nodo.machine_points}")
    canvas.after(400, draw_map)


def seleccionaEstadoInicial(modalidad):
    global nodo
    button_est_ingresar.place_forget()
    button_est_generar.place_forget()
    button_dif_principiante.pack(pady=20)
    button_dif_principiante.place(x=200, y=15)

    button_dif_amateur.pack(pady=20)
    button_dif_amateur.place(x=360, y=15)

    button_dif_experto.pack(pady=20)
    button_dif_experto.place(x=500, y=15)
    label_estado.pack(pady=20)
    label_estado.place(x=30, y=15)

    if modalidad == "Ingresar estado":
        nodo = Nodo(state=estado_inicial_ing)
    else:
        estado_inicial_gen = ['0'] * 64
        for num in range(1, 10):
            posicion = random.randint(0, 63)
            while estado_inicial_gen[posicion] != '0':
                posicion = random.randint(0, 63)
            estado_inicial_gen[posicion] = str(num)
        estado_inicial_gen = ''.join(estado_inicial_gen)
        nodo = Nodo(state=estado_inicial_gen)
    draw_map()


#
button_dif_principiante, button_dif_amateur, button_dif_experto = \
    tk.Button(root, text="Principiante", command=lambda: iniciarJuego("Principiante")), \
        tk.Button(root, text="Amateur", command=lambda: iniciarJuego("Amateur")), \
        tk.Button(root, text="Experto", command=lambda: iniciarJuego("Experto"))

button_est_generar = tk.Button(root, text="Generar estado", command=lambda: seleccionaEstadoInicial("Generar estado"))
button_est_ingresar = tk.Button(root, text="Ingresar estado",
                                command=lambda: seleccionaEstadoInicial("Ingresar estado"))

button_est_generar.pack(pady=20)
button_est_generar.place(x=190, y=15)

button_est_ingresar.pack(pady=20)
button_est_ingresar.place(x=340, y=15)
def reiniciarJuego():
    canvas.delete("all")
    label_estado.place_forget()
    label_estado.config(text="Dificultad: ")
    button_reinicio.place_forget()
    button_est_generar.place(x=190, y=15)
    button_est_ingresar.place(x=340, y=15)

# respuesta = easygui.buttonbox("Seleccione la dificultad:", choices=["Principiante", "Amateur", "Experto"])
label_estado = tk.Label(root, text="Dificultad: ", font=("Verdana", 12))
button_reinicio = tk.Button(root, text="Reiniciar", command=reiniciarJuego)
root.mainloop()


