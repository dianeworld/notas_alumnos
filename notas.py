# Diccionario con alumnos y sus notas
alumnos = {
    'Manu': 9.9,
    'Xavier': 7.2,
    'Franco': 7,
    'German': 9,
    'Alex': 7.4,
    'Adeel': 7.6,
    'Oscar': 7,
    'Andreu': 9,
    'Javier': 6.9,
    'Mecano': 8,
    'Mary': 8.5,
    'Jose': 7.2,
    'Diana': 6.8
}

# Nueva funcionalidad: Calcular la media de las notas
def calcular_media(diccionario):
    return sum(diccionario.values()) / len(diccionario)

# Mostrar la lista de alumnos y sus notas
print('Lista de alumnos y sus notas:')
for alumno, nota in alumnos.items():
    print(f'{alumno}: {nota}')


# Mostrar la nota media
media = calcular_media(alumnos)
print(f'\nNota media del grupo: {media:.2f}')

