#!/bin/bash

#Decodificando primero las imagenes

base64 --decode mystery_img1.txt > imgmisterio1.png
base64 --decode mystery_img2.txt > imgmisterio2.png
echo "las imagenes se han decodificado, revisar carpeta"

#Decodificando el hola mundo en C

base64 hola_mundo.c > textoC.txt
echo "el archivo ya debio codificarse, revisar carpeta"


