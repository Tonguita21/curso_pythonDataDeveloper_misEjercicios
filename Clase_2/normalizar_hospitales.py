import csv
archivo_in = open('hospitales.csv',encoding=('utf-8'))
archivo_out = open('hospitalesOut.csv','w', encoding=('utf-8'))

for linea in archivo_in:
    linea = linea.strip('\n')
    lista = linea.split(',')
    #print (lista)
    archivo_out.write(lista[0] + ',' + lista[7] + ',' + lista[2] + '\n')
    
archivo_in.close()    
archivo_out.close()