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