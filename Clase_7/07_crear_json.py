import json
import pprint

# with open('amo.json') as archivo:
# with open('C:/Users\groces\OneDrive - Galicia Seguros S.A\Desktop\Curso Data developer\Clase 7\amo.json') as archivo:
archivo = open('amo.json')    
amo = json.load(archivo)
    
pprint.pprint(amo)