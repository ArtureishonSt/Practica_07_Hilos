import threading
import tkinter as tk
from PIL import Image, ImageTk
import time


# Función para mover la imagen de izquierda a derecha
def move_horizontal(image_label, x_increment, sleep_time):
    while True:
        current_x = image_label.winfo_x()
        new_x = current_x + x_increment
        canvas.coords(image_label, new_x, image_label.winfo_y())
        time.sleep(sleep_time)


# Función para mover la imagen de arriba hacia abajo
def move_vertical(image_label, y_increment, sleep_time):
    while True:
        current_y = image_label.winfo_y()
        new_y = current_y + y_increment
        canvas.coords(image_label, image_label.winfo_x(), new_y)
        time.sleep(sleep_time)


# Crear la ventana principal
root = tk.Tk()
root.title("Movimiento de Imágenes")

# Crear un lienzo para las imágenes
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Cargar las imágenes
image1 = Image.open("imagen1.png")  # Reemplaza "imagen1.png" con el nombre de tu primera imagen
photo1 = ImageTk.PhotoImage(image1)
image_label1 = canvas.create_image(50, 50, anchor=tk.NW, image=photo1)

image2 = Image.open("imagen2.png")  # Reemplaza "imagen2.png" con el nombre de tu segunda imagen
photo2 = ImageTk.PhotoImage(image2)
image_label2 = canvas.create_image(150, 150, anchor=tk.NW, image=photo2)

# Crear y ejecutar los hilos para el movimiento de las imágenes
thread1 = threading.Thread(target=move_horizontal, args=(image_label1, 5, 0.05))
thread2 = threading.Thread(target=move_vertical, args=(image_label2, 5, 0.05))

thread1.start()
thread2.start()

# Iniciar el bucle principal de la aplicación
root.mainloop()
