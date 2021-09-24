import csv
archivo_in = open('peliculas.csv',encoding=('utf-8'))
tabla = csv.reader(archivo_in, delimiter = ',')
#archivo_out = open('subtes_salida.csv','w', encoding=('utf-8'))

for linea in archivo_in:
    linea = linea.strip('\n')
    lista = linea.split(',')
    print (lista)
    #archivo_out.write(lista[1] + ',' + lista[0] + ',' + lista[2] + '\n')
    
archivo_in.close()    
#archivo_out.close()