import requests
import json
import pprint

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/hospitales/hospitales.geojson'
contenido = requests.get(url).text
objeto = json.loads(contenido)
pprint.pprint(objeto)

# for hospital in objeto['Feature']:
for i in range(len(objeto['features'])):
    nombre = objeto['features'][i]['properties']['NOMBRE']
    nombre = objeto['features'][i]['properties']['NOMBRE']
    print (nombre)