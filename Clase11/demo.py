# -- de flask importamos la funcion Flask (F MAYUSCULAS) y json, 
from flask import Flask, json 

# -- la variable __name__ tiene asociado el nombre del archivo 
app = Flask(__name__)

print (app)

# -- armamos la ruta de la app
# -- La contrabarra indica que es el directorio raiz 
@app.route("/")

# -- creamos la funcion home. Esto se va a ejecutar en el localhost
def home():
    return "hola mundo desde la home de <b>flask</b>"

app.run(port = 3000, host = "0.0.0.0")

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

# print(app)


