# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 09:20:43 2021
LA idea del ejercicio es realizar scraping a la pagina ambito.com
y obtener los titulos de las noticias e informarlas en un csv.
@author: GRoces
 """
 
from bs4 import BeautifulSoup as BS
import requests
import csv
 
url = 'https://www.ambito.com/'
respuesta = requests.get(url)
respuesta.encoding = 'utf-8'
html = respuesta.text
dom = BS( html, features='html.parser')

titulos = dom.find_all(class_='title')

# -- Creo una lista de listas. El primer elemento (encabezados) genera una lista-
# -- Tiene que ir si o si con doble corchetes.
tabla = [['nro','titulo','link']]

for i in range(len(titulos)):
    titulo = titulos[i]
    link = titulos[i].a['href']
    print(i + 1, titulo.text, link)
    # -- Creo una fila y luego se la agrego a la tabla
    fila = [i + 1, titulo.text, link]
    tabla.append(fila)

# print(tabla)

with open('noticiasAmbito.csv','w', newline='') as file:
    salida = csv.writer(file)
    salida.writerows(tabla)


 

