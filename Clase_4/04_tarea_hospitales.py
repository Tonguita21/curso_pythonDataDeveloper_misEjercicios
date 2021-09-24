import requests
import mysql.connector
from io import StringIO

def insertarHospital(conexion, nombre, direccion, latitud, longitud):
    try:
        cursor = conexion.cursor()    
        query = 'INSERT INTO hospitales (nombre,	direccion,latitud,longitud) VALUES (%s,%s,%s,%s)'
        cursor.execute(query,(nombre, direccion, latitud, longitud))
        conexion.commit()
        cursor.close()
        return True
    except :
        return False

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
        
        if (insertarHospital(conexion,nombre,direccion,latitud,longitud)==True):
            lineasError.add (nroLinea)

        
        #print(nombre, direccion, latitud, longitud)
    except:
        lineasError.add (nroLinea)
        
for error in lineasError:
    LineasConError = LineasConError + str(error) + ', '

if (length(LineasConError) > 0):        
    print ('Se detectaron errores en las siguientes lineas: ' + LineasConError)
    
conexion.close()

# print(respuesta.text)

# contenido = respuesta.text
# with open ('peliculasCsv_out','w') as archivoSalida:
    # archivoSalida.write(contenido)


# print (contenido)