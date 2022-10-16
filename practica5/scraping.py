from bs4 import BeautifulSoup
import requests
import pandas as pd

link = 'https://www.wikidex.net/wiki/Espeon'

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
print (df)

df.to_csv('Informacion final P5.txt', index=False)
