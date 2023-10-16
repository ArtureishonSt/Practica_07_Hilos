import threading
import tkinter as tk
from PIL import Image, ImageTk
import time


class CustomImage:
    def __init__(self, canvas, x, y, image_path):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = canvas.create_image(x, y, anchor=tk.NW, image=self.photo)

    def move_horizontal(self, x_increment, sleep_time):
        while True:
            self.x += x_increment
            self.canvas.coords(self.image_label, self.x, self.y)
            time.sleep(sleep_time)

    def move_vertical(self, y_increment, sleep_time):
        while True:
            self.y += y_increment
            self.canvas.coords(self.image_label, self.x, self.y)
            time.sleep(sleep_time)


# Crear la ventana principal
root = tk.Tk()
root.title("Movimiento de Imágenes")

# Crear un lienzo para las imágenes
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Crear objetos CustomImage para las imágenes
image1 = CustomImage(canvas, 50, 50, "imagen1.png")  # Reemplaza "imagen1.png" con el nombre de tu primera imagen
image2 = CustomImage(canvas, 150, 150, "imagen2.png")  # Reemplaza "imagen2.png" con el nombre de tu segunda imagen

# Crear y ejecutar los hilos para el movimiento de las imágenes
thread1 = threading.Thread(target=image1.move_horizontal, args=(5, 0.05))
thread2 = threading.Thread(target=image2.move_vertical, args=(5, 0.05))

thread1.start()
thread2.start()

# Iniciar el bucle principal de la aplicación
root.mainloop()
