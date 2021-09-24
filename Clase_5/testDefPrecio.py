import requests
from bs4 import BeautifulSoup as BS

def obtener_precio(url_precio):
    try:
        precio = 0
        respuesta_precio = requests.get(url_precio)
        html_precio = respuesta_precio.text
        dom_precio = BS(html_precio, features='html.parser')
        linea = dom_precio.find(attrs={'id':'ctl00_ContentPlaceHolder1_rptFicha_ctl00_meta_price'})
        precio = linea['content']
        return precio
    except :
        return 0

url = 'https://www.cuspide.com/Libro/9789877363326/Una+Familia+Anormal'

precio = obtener_precio(url)
print(precio)