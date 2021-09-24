import requests
import csv
from io import StringIO

url = 'https://eant.tech/cursos/recursos/peliculas.csv'
respuesta = requests.get(url)
contenido = respuesta.text
with open ('peliculasCsv_out','w') as archivoSalida:
    archivoSalida.write(contenido)


# print (contenido)
