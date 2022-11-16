import tkinter as tk
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests
import pandas as pd

Ventana = tk.Tk ()
Ventana.title ("Practica 11")
Ventana.geometry("300x200")

Etiqueta1 = tk.Label(Ventana, text= "Descripcion de Pokedex segunda generacion", bg = "orange")
Etiqueta1.pack(fill = tk.X)
Etiqueta2 = tk.Label(Ventana, text= "Introduce el nombre del Pokemon")
Etiqueta2.pack(side = tk.LEFT)
Etiqueta3 = tk.Label(Ventana, text= "Recuerde solo Pokemon de la segunda generacion")
Etiqueta3.place(x=5, y =30)


Ctexto = tk.Entry(Ventana)
Ctexto.pack(side = tk.RIGHT)

def Resultado():
    Poke = Ctexto.get()
    link = 'https://www.wikidex.net/wiki/' + Poke

    pag = requests.get(link)
    soup = BeautifulSoup(pag.content, 'html.parser')

    jue = soup.find_all('th', class_='tfx-w enlacesblancos')
    juego = list()
    cnt = 0

    for i in jue:
        if cnt < 26:
            juego.append(i.text)
        else:
            break
        cnt += 1

    #Nota: la pagina maneja la clase de las celdas de estos 4 elementos de manera
    #diferente a como lo hace con el resto, esto debido a estetica, no encontre una
    #una forma de insertarlas en la lista usando el ciclo asi que las inserte directo
    juego.insert(14, 'Blanco')
    juego.insert(16, 'Blanco 2')
    juego.insert(23, 'Ultrasol')
    juego.insert(24, 'Ultraluna')

    info = soup.find_all('td', class_='tfx-fw')
    desc = list()
    cnt = 0

    for i in info:
        if cnt < 30:
            desc.append(i.text)
        else:
            break
        cnt += 1


    df = pd.DataFrame({'Juego': juego, 'Descripcion pokedex': desc})
    

    df.to_csv('Descripciones del Pokemon.txt', index=False)
    messagebox.showinfo("Resultado", "Se ha creado un archivo con la informacion obtenida")
    

btn1 = tk.Button(Ventana, text = "Aceptar", command = Resultado)
btn1.pack()
btn1.place(x=10, y=130)

Ventana.mainloop()
