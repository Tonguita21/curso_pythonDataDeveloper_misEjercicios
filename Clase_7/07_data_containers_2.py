import pprint


def agregar_mascota(nombre, tipo, raza):
     mascota = {'nombre': nombre,
                'tipo': tipo,
                'raza': raza}
     mascotas.add (mascota)
        
agregar_mascota('Rocco','perro','labrador')
agregar_mascota('Coco','gato','callejero')
agregar_mascota('lola','tortuga','tortuga')

#Diccionario
# perro = {'nombre': 'Rocco',
#          'tipo': 'perro',
#          'raza': 'labrador'}
#Variable
edad = 5

#Lista
le_gusta = ['Comer', 'Ladrar', 'Correr a las palomas']

#Combinación
perro.update({'edad': edad, 'le gusta': le_gusta})

#pprint.pprint(perro)

amo = {'nombre': 'Juan Carlos',
       'tipo': 'humano',
       'le gusta': ['Una buena conversación', 'Los fichines', 'Fútbol'],
       'edad': 38,
       'mascota': perro}

pprint.pprint(amo)


















