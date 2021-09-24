from bs4 import BeautifulSoup as BS

archivo_html = open('web_ejemplo.html', encoding='utf-8')

#parsea por medio de BeautifulSup el archivo y lo parsea de manera HTML
dom = BS(archivo_html, features = 'html.parser')

#print (dom.prettify()) #-- Muestra el dom con la estructura de html 

# -- si quiero obtener el primer link:
# primer_link = dom.a
# print(primer_link)

# -- Si queremos obtener el valor de algun campo en particular
# print(primer_link['class'])
# print(primer_link['href'])
# print(primer_link['id'])

# -- Otra manera de encontrar la etiqueta a:
# primer_link = dom.find('a')    
# print(primer_link)

# -- Con find_all obtenemos todas las etiquetas a(hipervinculos):
# Todos_los_link = dom.find_all('a')    
# for link in Todos_los_link:
#     print(link.string)
#     # print(link)

# #-- Obtener info por un ID
# parrafo = dom.find(id='otros-integrantes')
# # print(parrafo)

# # buscamos dentro de esa info todos los links
# links = parrafo.find_all('a')
# #-- pedimos una parte especifica de cada link
# print(links[0]['href'])

# -- Buscar por atributos standards: Buscar parrafo que tenga la clase = 'historia'
parrafo_historia = dom.find_all('p',class_ = 'historia')

# -- Buscar por atributos personalizados. 
parrafo_historia = dom.find_all('p', attrs={'class':'historia'})
print(parrafo_historia)

# -- Busqueda especifica por atributos. Se ponen como si fuera diccionario.
historia = dom.find(attrs={'data-minumero':'124124'})
print(historia)
