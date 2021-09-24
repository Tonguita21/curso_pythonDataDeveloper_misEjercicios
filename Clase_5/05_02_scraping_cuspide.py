# Obtener de cuspide.com los nombres de los 100 libros mas vendidos.
# De cada uno obtener el precio y luego almacenar en un archivo csv la info
from bs4 import BeautifulSoup as BS
import requests
import csv

def obtener_precio(url_precio):
    try:
        precio = 0
        respuesta_precio = requests.get(url_precio)
        html_precio = respuesta_precio.text
        dom_precio = BS(html_precio, features='html.parser')
        linea = dom_precio.find(attrs={'id':'ctl00_ContentPlaceHolder1_rptFicha_ctl00_meta_price'})
        precio = linea['content']
        return precio
    except :
        return 0

url = 'https://www.cuspide.com/cienmasvendidos'
respuesta = requests.get(url)

# nos aseguramos de tener el encoding correspondiente
respuesta.encoding = 'utf-8'

html = respuesta.text

# -- Obtengo en DOM todo el texto parseado como html para poder buscar la info en las etiquetas.
dom = BS(html, features='html.parser')

# -- Creo una lista de listas. El primer elemento (encabezados) genera una lista-
# -- Tiene que ir si o si con doble corchetes.
tabla = [['nro','titulo','precio','link']]

articulos = dom.find_all('article')

for i in range(len(articulos)):
    nro = i + 1
    titulo = articulos[i].figure.div.a['title']
    # Obtengo la url de la pagina del libro para obtener el precio del libro
    link = "https://www.cuspide.com" + articulos[i].figure.div.a['href']
    precio = obtener_precio(link)
    fila = [nro, titulo, precio, link]
    tabla.append(fila)
    
with open('librosCuspide.csv','w', newline='') as file:
    salida = csv.writer(file)
    salida.writerows(tabla)