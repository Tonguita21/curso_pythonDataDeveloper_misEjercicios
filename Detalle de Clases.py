#Detalle de Clases 

#-------------
#-- Clase 1:
#-------------
#Manejo de archivos
#FOR
#STRIP
#SPLIT (separa el texto por el carácter pasado por parámetro)
#Encoding
#print
#Leer archivo, generar otro de salida, alterando los campos

#-------------
#-- Clase 2:
#-------------
#Normalización de datos
#modulo datetime (strptime, strftime) 
#Posix

#-------------
#-- Clase 3:
#-------------
#Base de datos 
#Select, insert, delete

#------------------------------------------------------------
#03_01_select_alumnos_printPorPantalla.py
#------------------------------------------------------------
#codigos de respuesta
#mysql.connector
#------------------------------------------------------------
import mysql.connector

with open('C:/Users\gonza\Documents\Trabajo\EANT\Python\claves_mysql.txt') as claves:
   #claves_mysql = [clave for clave in claves]
   claves_mysql = []
   for clave in claves:
      claves_mysql.append(clave)

conexion = mysql.connector.connect(host = claves_mysql[0],
                                   database = claves_mysql[1],
                                   user = claves_mysql[2],
                                   password = claves_mysql[3])

cursor = conexion.cursor()

query = 'SELECT nombre, apellido FROM alumnos'
cursor.execute(query)

alumnos = cursor.fetchall()
for alumno in alumnos:
    print(alumno[0])
   
cursor.close()
conexion.close()


#----------------------------
#-- Creacion de tabla alumnos
#-------------
CREATE TABLE alumnos(
alumnos_id integer not null primary key
,nombre varchar(50) not null
,apellido varchar(50) not null
,dni integer
,email varchar(100) not null
,fecha_nac date)




#-------------
#-- Clase 4:
#-------------
#Datos en la nube
#Request

#------------------------------------------------------------
#04_01_web_ejemplo.py
#------------------------------------------------------------
#codigos de respuesta
#Requests
#------------------------------------------------------------
import requests

url = 'https://eant.tech/cursos/recursos/frutas.txt'

respuesta = requests.get(url)

print ("Codigo de respuesta:", respuesta.status_code)
print ("URL:", respuesta.url)
print ("Contenido del responde:", respuesta.content)
print ("Contenido del responde:", respuesta.text)
print ("Encoding de la respuesta:", respuesta.encoding)
respuesta.encoding = 'utf-8'
print ("Encoding de la respuesta:", respuesta.encoding)
print ("Contenido del responde:", respuesta.text)

#------------------------------------------------------------
#04_02_consultaWeb_generaCSV.py
#------------------------------------------------------------
#codigos de respuesta
#Requests, CSV, IO (StringIO) 
#Lee una web, obtiene el contenido y lo almacena en un csv
#------------------------------------------------------------
import requests
import csv
from io import StringIO

url = 'https://eant.tech/cursos/recursos/peliculas.csv'
respuesta = requests.get(url)
contenido = respuesta.text
with open ('peliculasCsv_out','w') as archivoSalida:
    archivoSalida.write(contenido)


#------------------------------------------------------------
#04_tarea_hospitales.py
#------------------------------------------------------------
#Obtiene info de la web buenos aires data (hospitales)
#La recorre y por cada registro inserta en BD
#
#------------------------------------------------------------
import requests
import mysql.connector
from io import StringIO

def insertarHospital(conexion, nombre, direccion, latitud, longitud):
    try:
        cursor = conexion.cursor()    
        query = 'INSERT INTO hospitales (nombre,	direccion,latitud,longitud) VALUES (%s,%s,%s,%s)'
        cursor.execute(query,(nombre, direccion, latitud, longitud))
        conexion.commit()
        cursor.close()
        return True
    except :
        return False

nroLinea = 0

#-- Armo la conexion a mySql --
conexion = mysql.connector.connect(host= 'sql5.freemysqlhosting.net', database = 'sql5428931', user = 'sql5428931', password = '5FhkfwA5BH')

#-- Obtengo los datos de los hospitales de la pagina Buenos Aires Data --
url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/hospitales/hospitales.csv'
respuesta = requests.get(url)

#-- Paso el encoding a UTF-8
respuesta.encoding = 'utf-8'

#-- Utilizo StringIO para que el texto que devuelve como respuesta lo pueda tratar como un archivo
contenido = StringIO(respuesta.text)

#-- Hago un next para evitar insertar los titulos
next(contenido)

for linea in contenido:
    try:
        nroLinea = nroLinea + 1
        
        #-- Separo los campos del registro por "," para poder obtener solo los que necesitamos 
        linea = linea.split(',')
        nombre = linea[2]
        direccion = linea[5] + ' ' + linea[6].replace('"','')
        coordenadas = linea[0][7:-1].split()
        latitud = coordenadas[0].replace('(','')
        longitud = coordenadas[1].replace(')','')
        
        if (insertarHospital(conexion,nombre,direccion,latitud,longitud)==True):
            lineasError.add (nroLinea)

        
        #print(nombre, direccion, latitud, longitud)
    except:
        lineasError.add (nroLinea)
        
for error in lineasError:
    LineasConError = LineasConError + str(error) + ', '

if (length(LineasConError) > 0):        
    print ('Se detectaron errores en las siguientes lineas: ' + LineasConError)
    
conexion.close()




#-------------
#-- Clase 5:
#-------------
#Beautifull Soup 4

#------------------------------------------------------------
#05_01_web_ejemplo.py
#------------------------------------------------------------
#Este ejercicio busca info de una pagina html, buscando info
#por etiquetas, por ID, por atributos, etc
#------------------------------------------------------------
from bs4 import BeautifulSoup as BS

archivo_html = open('web_ejemplo.html', encoding='utf-8')

#parsea por medio de BeautifulSup el archivo y lo parsea de manera HTML
dom = BS(archivo_html, features = 'html.parser')

#print (dom.prettify()) #-- Muestra el dom con la estructura de html 

# -- si quiero obtener el primer link:
# primer_link = dom.a
# print(primer_link)

# -- Si queremos obtener el valor de algun campo en particular
# print(primer_link['class'])
# print(primer_link['href'])
# print(primer_link['id'])

# -- Otra manera de encontrar la etiqueta a:
# primer_link = dom.find('a')    
# print(primer_link)

# -- Con find_all obtenemos todas las etiquetas a(hipervinculos):
# Todos_los_link = dom.find_all('a')    
# for link in Todos_los_link:
#     print(link.string)
#     # print(link)

# #-- Obtener info por un ID
# parrafo = dom.find(id='otros-integrantes')
# # print(parrafo)
# # buscamos dentro de esa info todos los links
# links = parrafo.find_all('a')
# #-- pedimos una parte especifica de cada link
# print(links[0]['href'])

# -- Buscar por atributos standards: Buscar parrafo que tenga la clase = 'historia'
parrafo_historia = dom.find_all('p',class_ = 'historia')

# -- Buscar por atributos personalizados. 
parrafo_historia = dom.find_all('p', attrs={'class':'historia'})
print(parrafo_historia)

# -- Busqueda especifica por atributos. Se ponen como si fuera diccionario.
historia = dom.find(attrs={'data-minumero':'124124'})
print(historia)


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
#------------------------------------------------------------
#05_02_scraping_cuspide.py
#------------------------------------------------------------
# La idea del ejercicio es realizar scraping a la pagina cuspide.com,
# Obtener de cuspide.com los nombres de los 100 libros mas vendidos.
# De cada uno obtener el precio y luego almacenar en un archivo csv la info
# Utiliza request, beautifulsoap bs4 y CSV
#------------------------------------------------------------
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

#------------------------------------------------------------
#05_03_scraping_ambito_generandocsv.py
#------------------------------------------------------------
# La idea del ejercicio es realizar scraping a la pagina ambito.com,
# obtener los titulos de las noticias e informarlas en un csv.
# Utiliza request, beautifulsoap bs4 y tabla (lista de listas)
# Ambito muestra el DOM automaticamente
#------------------------------------------------------------
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

#-------------
#-- Clase 6:
#-------------
#scraping
#Selenium

#------------------------------------------------------------
#06_01_scraping_olx.py
#------------------------------------------------------------
# La idea del ejercicio es realizar scraping a la pagina olx.com,
# obtener los titulos y precios de los productos para una busqueda especifica
# para obtener el DOM de OLX es necesario hacer click en el boton "siguiente" mediante scripts JS
# Utiliza selenium para poder ejecutar scripts de javascript y beautifulsoap bs4
# Utiliza Time (sleep) para esperar a que cargue la pagina
#------------------------------------------------------------

from bs4 import BeautifulSoup as BS
# Utilizamos selenium para poder tener la posibilidad 
# de ejecutar scripts JS en la pagina a analizar.
from selenium import webdriver
from time import sleep

# abrimos con el driver el navegador mostrando en browser
# driver = webdriver.Chrome('chromedriver.exe')

# Para no abrir el browser las opciones son las siguientes:
# creamos el objeto de opciones para el navegador.
options = webdriver.ChromeOptions()

# le pasamos el argumento headless a las opciones para que no lo abra 
# options.add_argument('headless')

# para abrir el browser en modo incognito
options.add_argument('--incognito')

# abrimos con el driver el navegador
driver = webdriver.Chrome('chromedriver.exe', options = options)

# Por medio del driver ya estamos en condiciones de ejecutar scripts
# driver.execute_script('alert("Hola mundo")')

# Asignamos al driver que contiene el navegador la url a analizar
driver.get('https://www.olx.com.ar/items/q-aspiradora-auto')
# driver.get('https://www.olx.com.ar/items/q-peugeot-408-hdi')

sleep(3)

# Armamos scripts en JS para ejecutarlos en la pagina.
script_js = """
let boton =  document.querySelector('[data-aut-id="btnLoadMore"]')
if(boton){
        boton.click()
        }
else {
      return "No existe"
      }
"""

while driver.execute_script(script_js) != "No existe":
    sleep(3)
    
sleep(2)    
# Capturamos el HTML de la pagina
html = driver.execute_script('return document.documentElement.outerHTML')

dom = BS(html,'html.parser')

# Capturo todos los productos de la pagina.
productos = dom.find_all(class_="IKo3_")

nro = 1
# recorro todos los productos y capturo la descripcion y su precio
for producto in productos:
    descripcion = producto.find(class_="_2tW1I").string
    precio = producto.find(class_="_89yzn").string
    print (nro, descripcion, precio)
    nro += 1 

#driver.quit()


#------------------------------------------------------------
#06_01_scraping_olx.py
#------------------------------------------------------------
# Para obtener el DOM de la nacion es necesario ejecutar un 
# script JS para que haga scroll de la pagina completa 
# obteniendo la pos actual y el fin de pagina. 
# Utiliza selenium para poder ejecutar scripts de javascript y beautifulsoap bs4
# Utiliza Time (sleep) para esperar a que cargue la pagina
# Abre la pagina en modo incognito
# Script para realizar scroll en la pagina
#------------------------------------------------------------


from bs4 import BeautifulSoup as BS
from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome('C:/Users\gonza\Documents\Trabajo\EANT\Python\chromedriver.exe', options = options)

#driver.execute_script('alert("Hola Mundo")')
driver.get('https://www.lanacion.com.ar/')

sleep(3)

script_scroll_js = """
   let fin_pantalla = document.body.scrollHeight
   window.scrollTo(0, fin_pantalla)
   return fin_pantalla
   
"""
pos_actual = 0
pos_siguiente = driver.execute_script(script_scroll_js)
sleep(3)

while pos_actual != pos_siguiente:
   pos_actual = pos_siguiente
   pos_siguiente = driver.execute_script(script_scroll_js)
   sleep(3)
   print(pos_actual)
   
print("Llegamos al final de la página")

html = driver.execute_script("return document.documentElement.outerHTML")

driver.quit()

dom = BS(html, 'html.parser')
titulares = dom.find_all(class_="com-title --xs")
for titular in titulares:
   titulo = titular.a.text
   link  = titular.a['href']
   print(titulo, link)
   print()



#-------------
#-- Clase 7:
#-------------
#Data Containers (variables, listas y diccionarios)
#Json
#Lectura de archivos de API's
