import requests
import mysql.connector
from io import StringIO

def insertarHospital(conexion, nombre, direccion, latitud, longitud):
    resultado = True
    try:
        cursor = conexion.cursor()    
        query = 'INSERT INTO hospitales (nombre,	direccion,latitud,longitud) VALUES (%s,%s,%s,%s)'
        cursor.execute(query,(nombre, direccion, latitud, longitud))
        conexion.commit()
        cursor.close()
        
    except :
        resultado = False
    return resultado

lineasError = []
LineasConError=''
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
        
        #-- Llamo a la funcion que me inserta en la BD
        if (insertarHospital(conexion,nombre,direccion,latitud,longitud)==False):
            lineasError.append(nroLinea)

    except:
        #En el caso de error en alguna linea las voy agregando en una coleccion para luego informar los errores
        lineasError.append(nroLinea)
        
for error in lineasError:
    LineasConError = LineasConError + str(error) + ', '

if len(LineasConError) > 0:  
    final_lineasConError = LineasConError[:-1]     
    print ('Se detectaron errores en las siguientes lineas: ' + final_lineasConError)
    
conexion.close()
