import requests
import json
from pprint import pprint

# key = 'e1e730bcfd663345bcbae4e65f832288'

with open('C:/Users\groces\OneDrive - Galicia Seguros S.A\Desktop\Curso Data developer\claves.txt') as claves: 
    keys = [clave.strip('\n') for clave in claves] 
    
key = keys[0]

# with open('sucursales_sol_360.csv') as suc: 
archivo_in = open('sucursales_sol_360.csv')

for linea in archivo_in:
    linea = linea.strip('\n')
    # print (ciudad.replace(";",", "))
    ciudad = linea.split(';')
    # print (ciudad[0] + )
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + ciudad[0] + ", Argentina&appid=" + key
    objeto = json.loads(requests.get(url).text)
    pprint(objeto)
    # lat = objeto['results'][0]['geometry']['lat']
    # lon = objeto['results'][0]['geometry']['lng']
    # pprint(lat,lon)

# # print(key) 



# # url = "http://api.openweathermap.org/data/2.5/weather?q=" + ciudad + "&units=metric&lang=es&appid" + key
# url = "http://api.openweathermap.org/data/2.5/weather?q=" + ciudad + "&appid=" + key

# objeto = json.loads(requests.get(url).text)

# pprint(objeto)

