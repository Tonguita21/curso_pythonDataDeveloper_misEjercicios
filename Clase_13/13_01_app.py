
# -- de flask importamos la funcion Flask (F MAYUSCULAS) y json, 
from flask import Flask, json 
# -- fue necesario instalar pip install pymongo[srv] para poder acceder a la BD de mongo
# -- en un repositorio remoto (no local host)
from pymongo import MongoClient

# Importamos el archivo que me levanta las variables de entorno
import settings
from os import environ

USER = environ['DB_USER']
PASS = environ['DB_PASS']
HOST = environ['DB_HOST']
BASE = environ['DB_NAME']

# -- la variable __name__ tiene asociado el nombre del archivo 
app = Flask(__name__)

# -- Mongo db -- 
client = MongoClient("mongodb+srv://eant-groces:Gaston21@pdd-lm-n-297.r4bmn.mongodb.net/api-twitter?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")


# client = pymongo.MongoClient("mongodb+srv://eant-groces:Gaston21@pdd-lm-n-297.r4bmn.mongodb.net/pdd-lm-n-297?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE
# ")

@app.route("/tweets")
def getTweets():
    twitter = client['api-twitter']['tweets']
    
    users = twitter.find()
    
    for user in users:
        print(user)
        
    return "mira la consola..."


# -- armamos la ruta de la app
# -- La contrabarra indica que es el directorio raiz 
@app.route("/")

# -- creamos la funcion home. Esto se va a ejecutar en el localhost
def home():
    return "hola mundo desde la home de <b>flask</b>"

# -- Asignamos un puerto a la app
# -- Un puerto seria como un nro de interno 
# -- EL puerto 3000 se va acceder al servicio de flask
# -- Con esto estamos haciendo correr nuestro servidor web en el puerto 3000
# -- Running on http://127.0.0.1:3000/
# app.run(port = 3000)

# -- agregamos una nueva ruta para users de twitter
@app.route("/users")
def usersTwitter():
    users = [
        { "name" : "smessina_" },
        { "name" : "eanttech"}
        ]
    
    # -- json.dumps le da formato de json a la coleccion / diccionario
    response = app.response_class(response = json.dumps(users), status = 200 , mimetype = "application/json") 
    
    return response  

# -- Asignamos una intranet
app.run(port = 3000, host = "0.0.0.0")