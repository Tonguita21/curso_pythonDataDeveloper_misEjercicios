

#----  Librerias -----#

from bs4 import BeautifulSoup
import requests
import unicodedata
from flask import Flask, json 
from pprint import pprint


app = Flask(__name__)


@app.route("/<paramLugar>/<paramTipoProp>/<paramTipoOp>")
 # def getTweets(param1,paramTipoProp,paramTipoOp):
def getProps(paramLugar,paramTipoProp,paramTipoOp):
    
    numero_pagina = 1
    diccionario = []
    validacion = True
    
    while validacion:
        
        url = "https://www.properati.com.ar/s/" + paramLugar + "/" + paramTipoProp + "/" + paramTipoOp + "?page=" + str(numero_pagina)
        print('\n-------------')
        print('Numero de pagina ejecutada: ', numero_pagina)
        print('\n-------------')

        
        response = requests.get(url)
        response.encoding = "utf-8"
        html = response.text
        dom = BeautifulSoup(html, features = "html.parser")
        
        clase_final = dom.find( attrs = { 'class' : 'StyledEmptyListing-sc-1p4fosb-0 hhzlFS' } )
        
        if clase_final != None:
            validacion = False
        else:
            conteo = 0
            anuncios = dom.find_all( attrs = { 'class' : 'StyledCardInfo-n9541a-2 fETDIw' } )
            for anuncio in anuncios:
                titulo = anuncio.find( attrs = { 'class' : 'StyledTitle-n9541a-4 beEJHC' } )
                precio = anuncio.find( attrs = { 'class' : 'StyledPrice-n9541a-5 jcqxPh' } )
                expensas = anuncio.find( attrs = { 'class' : 'StyledMaintenanceFees-n9541a-6 bXXZTB' } )
                detalles = anuncio.find( attrs = { 'class' : 'StyledInfoIcons-n9541a-9 fFZRGK' } )
                inmobiliaria = anuncio.find( attrs = { 'class' : 'seller-name' } )
                conteo += 1
                if titulo: titulo = titulo.get_text()
                if precio: precio= precio.get_text()
                if expensas: expensas = unicodedata.normalize("NFKD", expensas.get_text()) 
                if expensas == None:
                       expensas = 'No tiene expensas'
                if inmobiliaria: inmobiliaria = inmobiliaria.get_text()
                if detalles:
                    spans = detalles.find_all('span')
                    for span in spans:
                        txt = span.get_text()
                        if (txt.find('m²')>=0): m2 = txt
                        if (txt.find('ambiente')>=0 or txt.find('ambientes')>=0): ambientes = txt
                        else:
                            ambientes = 'No figura'
                        if (txt.find('baño')>=0): banios = txt
                caracteristicas = {'Titulo': titulo, 'Precio': precio, 'Expensas':expensas, 'Inmobiliaria':inmobiliaria, 'm2':m2.strip('m²'), 
                             'Sanitarios':banios.strip('baño').strip('baños'), 'Ambientes':ambientes}
            diccionario.append(caracteristicas)   
            numero_pagina += 1

              

#     # -- Se retorna el valor de result en formato json            
    return app.response_class(response = json.dumps(diccionario), status = 200 , mimetype = "application/json")


# -- Asignamos una intranet
app.run(port = 3000, host = "0.0.0.0")




