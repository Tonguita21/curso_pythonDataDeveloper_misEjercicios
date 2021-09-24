from bs4 import BeautifulSoup as BS
# Utilizamos selenium para poder tener la posibilidad 
# de ejecutar scripts JS en la pagina a analizar.
from selenium import webdriver
from time import sleep

# abrimos con el driver el navegador mostrando en browser
# driver = webdriver.Chrome('chromedriver.exe')

# Para no abrir el browser las opciones son las siguientes:
# creamos el objeto de opciones para el navegador.
options = webdriver.ChromeOptions()

# le pasamos el argumento headless a las opciones para que no lo abra 
# options.add_argument('headless')

# para abrir el browser en modo incognito
options.add_argument('--incognito')

# abrimos con el driver el navegador
driver = webdriver.Chrome('chromedriver.exe', options = options)

# Por medio del driver ya estamos en condiciones de ejecutar scripts
# driver.execute_script('alert("Hola mundo")')

# Asignamos al driver que contiene el navegador la url a analizar
driver.get('https://www.olx.com.ar/items/q-aspiradora-auto')
# driver.get('https://www.olx.com.ar/items/q-peugeot-408-hdi')

sleep(3)

# Armamos scripts en JS para ejecutarlos en la pagina.
script_js = """
let boton =  document.querySelector('[data-aut-id="btnLoadMore"]')
if(boton){
        boton.click()
        }
else {
      return "No existe"
      }
"""

while driver.execute_script(script_js) != "No existe":
    sleep(3)
    
sleep(2)    
# Capturamos el HTML de la pagina
html = driver.execute_script('return document.documentElement.outerHTML')

dom = BS(html,'html.parser')

# Capturo todos los productos de la pagina.
productos = dom.find_all(class_="IKo3_")

nro = 1
# recorro todos los productos y capturo la descripcion y su precio
for producto in productos:
    descripcion = producto.find(class_="_2tW1I").string
    precio = producto.find(class_="_89yzn").string
    print (nro, descripcion, precio)
    nro += 1 

#driver.quit()


