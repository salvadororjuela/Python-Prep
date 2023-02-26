# 1. Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
ciudades = ["Bogota", "Quito", "Lima", "Buenos Aires", "Brasilia", "Montevideo", "La Paz", "Santiago", "Caracas", "Asuncion"]

# 2. Imprimir por pantalla el segundo elemento de la lista
print(ciudades[1])

# 3. Imprimir por pantalla del segundo al cuarto elemento
print(ciudades[1:4])

# 4. Visualizar el tipo de dato de la lista
print(type(ciudades))

# 5. Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
print(ciudades[0:])

# 6. Visualizar los primeros 4 elementos de la lista
print(ciudades[:4])

# 7. Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
ciudades.append("Bogota")
print(ciudades)

# 8. Agregar otra ciudad, pero en la cuarta posición
ciudades.insert(3, "Madrid")
print(ciudades)

# 9. Concatenar otra lista a la ya creada
europeas = ["Roma", "Londres", "Paris", "Berlin", "Berna"]
ciudades.extend(europeas)
print(ciudades)

# 10. Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
print(ciudades.index("Bogota"))

# 11. Qué pasa si se busca un elemento que no existe?
# R//: Mostrara un error

# 12. Eliminar un elemento de la lista
ciudades.remove("Lima")
print(ciudades)

# 13. ¿Qué pasa si el elemento a eliminar no existe?
# R//: Arroja el mismo error del punto 11
# ciudades.remove("Berna")

# 14. Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
eliminada = ciudades.pop()
print(eliminada)

# 15. Mostrar la lista multiplicada por 4
print(ciudades * 4)

# 16. Crear una tupla que contenga los números enteros del 1 al 20
numeros = list()

for i in range(1, 21):
    numeros.append(i)

tupNumeros = tuple(numeros)
print(tupNumeros)
print(type(tupNumeros))

# 17. Imprimir desde el índice 10 al 15 de la tupla
print(tupNumeros[10:16])

# 18. Evaluar si los números 20 y 30 están dentro de la tupla
if 20 in tupNumeros and 30 in tupNumeros:
    print("Si estan presentes")
else:
    print("O el 20 o el 30 no estan en la tupla")

# 19. Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
mexico = "Mexico DC"
if mexico in ciudades:
    print(f"{mexico} ya existe")
else:
    ciudades.append(mexico)
    print(f"Se agrego {mexico} a la lista")

print(ciudades)

# 20. Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
print(f"Bogota esta {ciudades.count('Bogota')} veces en la lista ciudades")
print(f"El numero 10 esta {tupNumeros.count(10)} veces en la tupla tupNumeros")

# 21. Convertir la tupla en una lista
listaNumeros = list(tupNumeros)
print(listaNumeros)
print(type(listaNumeros))

# 22. Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
uno, dos, tres, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, = tupNumeros
print(uno, dos, tres)

# 24. Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
dictCiudades = {
    "Ciudad": ciudades,
    "Pais": ["Colombia", "Ecuador",  "Espana",  "Argentina",  "Brasil", "Uruguay", "Bolivia", "Chile", "Venezuela", "Paraguay", "Colombia", "Italia", "Inglaterra", "Francia", "Alemania", "Mexico"],
    "Continente": ["America del Sur", "Europa"]
}
# 25. Imprimir las claves del diccionario
print(dictCiudades.keys())

# 26, Imprimir las ciudades a través de su clave
print(dictCiudades["Ciudad"])
