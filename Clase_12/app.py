
# -- de flask importamos la funcion Flask (F MAYUSCULAS) y json, 
from flask import Flask, json 
# -- fue necesario instalar pip install pymongo[srv] para poder acceder a la BD de mongo
# -- en un repositorio remoto (no local host)
from pymongo import MongoClient


# -- la variable __name__ tiene asociado el nombre del archivo 
app = Flask(__name__)

# -- Conexion a MongoDB --

# client = MongoClient("mongodb+srv://eant-groces:Gaston21@pdd-lm-n-297.r4bmn.mongodb.net/api-twitter?retryWrites=true&w=majority")
client = MongoClient("mongodb+srv://eant-groces:Gaston21@pdd-lm-n-297.r4bmn.mongodb.net/api-twitter?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")


# -- Agregamos la ruta tweets 
# @app.route("/tweets")

# -- Podemos configurar la ruta para que sea dinamica, reciba parametros
# -- y el mismo se envie a la funcion para tener logica en base al mismo
@app.route("/tweets/<param1>")

def getTweets(param1):
    
    twitter = client['api-twitter']['tweets']
 
    # users = twitter.find()
    
    # -- Agregamos la validacion del parametro para que esté dentro de los parametros esperados.
    # -- Caso contrario se informa Error
    if param1 not in ['people','company']:
        result = {'error':'categoria no disponible'}
    else:
        
        # -- Podemos pasarle el parametro para filtrar la informacion.
        users = twitter.find({'type' : param1})
        # users = twitter.find().limit(2)  -- En el caso de querer limitar
        
        # for user in users:
        #     print('------------------')
        #     print(user)
        # return "mira la consola..."
        
        result = []
        
        for user in users:
            item = { 'usuario': user['name']}
            result.append(item)
    
    # -- Se retorna el valor de result en formato json            
    return app.response_class(response = json.dumps(result), status = 200 , mimetype = "application/json")
  

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