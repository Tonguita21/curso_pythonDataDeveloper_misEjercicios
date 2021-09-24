import json
import requests
import pprint

# -- Obtenemos el json de la nube
url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/hospitales/hospitales.geojson'

# -- obtenemos el contenido de texto 
contenido = requests.get(url).text

# -- Transformamos el texto a json utilizando loads (la S significa que toma texto como entrada)
objeto = json.loads(contenido)

pprint.pprint(objeto['features'][0]['properties']['NOMBRE'])
pprint.pprint(objeto['features'][0]['properties']['CALLE'])

# objeto['features']