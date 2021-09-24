# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Parametros:
#1 = archivo
#2 = r = read,a = append, w = write
archivo = open("frutas.txt",'r',encoding='utf-8')

#Recorro el archivo
for linea in archivo:
    linea = linea.strip('\n')
    #linea = linea.replace('\n', '')   #reemplaza salto de line por espacio vacio
    #linea = linea[0:-1]  #-- corta el ultimo caracter
    print(linea)

archivo.close()