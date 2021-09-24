import csv

archivo_in = open('hospitales.csv', encoding = 'utf-8') 
entrada = csv.reader(archivo_in)
    #salida = csv.writer(archivo_out)
    #salida.writerow(['latitud','longitud','dirección','nombre'])
for linea in entrada:
    tabla = [linea[0], linea[5], linea[6], linea[2]]
    print(linea)
"""         point = linea[0]
        point_split = point.split(' ')
        latitud1 =str(point_split[2:3])
        latitud = latitud1.replace(')', '')
        latitud = latitud.strip('[')
        latitud = latitud.strip(']')
        longitud1 = str(point_split[1:2])
        longitud = longitud1.replace('(','')
        longitud = longitud.strip('[')
        longitud = longitud.strip(']')
        direccion = ', '.join([linea[5],linea[6]]) """
        #print(tabla[0])
        #salida.writerow([latitud,longitud,direccion,linea[2]])