import pprint

# creo el objeto perro.

# diccionario:
perro = {'nombre':'Uma',
         'tipo':'naa',
         'color':'marron claro'}    
# variable
edad = 7

# lista
le_gusta = ['correr','ladrar','comer']

# print(perro)

perro.update({'edad':edad})
perro.update({'le gusta':le_gusta})

# print(perro)
pprint.pprint(perro)

perro['le gusta']