import json
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# Cargar datos del archivo JSON
with open("plantas.json", "r", encoding="utf-8") as file:
    plantas = json.load(file)

# Función para mostrar detalles de una planta seleccionada
def mostrar_detalles(event):
    seleccion = lista_plantas.curselection()
    if seleccion:
        indice = seleccion[0]
        planta = plantas[indice]
        detalles_text.set(f"Nombre: {planta['nombre']}\n"
                          f"Nombre científico: {planta['nombre_cientifico']}\n"
                          f"Partes usadas: {planta['partes_usadas']}\n"
                          f"Usos internos: {planta['usos_tradicionales'].get('interno', 'N/A')}\n"
                          f"Usos externos: {planta['usos_tradicionales'].get('externo', 'N/A')}\n"
                          f"Efectos: {planta['efectos']}\n"
                          f"Precauciones: {planta['precauciones']}")
        
        # Cargar imagen de la planta
        ruta_imagen = f"imagenes/{planta['nombre']}.jpg"
        if os.path.exists(ruta_imagen):
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((200, 200))  # Redimensionar
            foto = ImageTk.PhotoImage(imagen)
            label_imagen.config(image=foto)
            label_imagen.image = foto
        else:
            label_imagen.config(image="", text="Imagen no disponible")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Plantas Medicinales")
root.geometry("700x500")

# Lista de plantas
lista_plantas = tk.Listbox(root, height=15)
lista_plantas.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
lista_plantas.bind("<<ListboxSelect>>", mostrar_detalles)

# Agregar nombres de plantas a la lista
for planta in plantas:
    lista_plantas.insert(tk.END, planta["nombre"])

# Panel de detalles
detalles_text = tk.StringVar()
label_detalles = ttk.Label(root, textvariable=detalles_text, justify=tk.LEFT, wraplength=400)
label_detalles.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Imagen de la planta
label_imagen = tk.Label(root, text="Imagen no disponible", bg="gray", width=200, height=200)
label_imagen.pack(side=tk.BOTTOM, padx=10, pady=10)

root.mainloop()
