# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:24:38 2021

@author: GRoces
"""

archivo_in = open('peliculas.csv',encoding=('utf-8'))
#archivo_out = open('subtes_salida.csv','w', encoding=('utf-8'))

for linea in archivo_in:
    linea = linea.strip('\n')
    lista = linea.split(',')
    print (lista)
    #archivo_out.write(lista[1] + ',' + lista[0] + ',' + lista[2] + '\n')
    
archivo_in.close()    
#archivo_out.close()