# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:24:38 2021

@author: GRoces
"""

archivo = open('subtes.csv',encoding=('utf-8'))

for linea in archivo:
    linea = linea.strip('\n')
    lista = linea.split(',')
    print (lista[2])
    
archivo.close()    