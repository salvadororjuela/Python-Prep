# 1. A partir de una lista vacía, utilizar un ciclo while para cargar allí
# números negativos del -15 al - 1
numerosInversos = list()
numeroAgregar = -15
while numeroAgregar < 0:
    numerosInversos.append(numeroAgregar)
    numeroAgregar += 1

print(numerosInversos)    

# 2. ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo
# los números pares?
contador = 0
while True:
    if contador == len(numerosInversos):
        break
    for i in numerosInversos:
        contador += 1
        if i % 2 == 0:
            print(i)

# 3. Resolver el punto anterior sin utilizar un ciclo while
numerosPares = [i for i in numerosInversos if i % 2 == 0]
print(f"Los numeros impares de la lista son: {numerosPares}")

# 4. Utilizar el iterable para recorrer sólo los primeros 3 elementos
iterable = iter(numerosPares)
print(next(iterable))
print(next(iterable))
print(next(iterable))

# 5. Utilizar la función enumerate para obtener dentro del iterable, tambien
# el índice al que corresponde el elemento
for i, j in enumerate(numerosPares):
    print(f"Index: {i} / numero: {j}")

# 6. Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo
# donde se completen los valores faltantes: lista = [1, 2, 5, 7, 8, 10, 13, 14,
# 15, 17, 20]
lista = [1, 2, 5, 7, 8, 10, 13, 14, 15, 17, 20]
for i in range(1, 21):
    if i not in lista:
        lista.append(i)
lista.sort()
print(lista)

# 7. La sucesión de Fibonacci es un listado de números que sigue la fórmula:
# n0 = 0
# n1 = 1
# ni = ni-1 + ni-2
# Crear una lista con los primeros treinta números de la sucesión.
fibonacci = [0, 1]
for i in range(28):
    nextNumber = fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2]
    fibonacci.append(nextNumber)
print(fibonacci)

# 8. Realizar la suma de todos elementos de la lista del punto anterior
print(f"""la suma de los primeros 30 numeros de la serie de
      Fibonacci es: {sum(fibonacci)}""")

# 9. La proporción aurea se expresa con una proporción matemática que nace el
# número irracional Phi = 1, 618… que los griegos llamaron número áureo. El
# cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del
# ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos
# números contiguos:
# Donde i es la cantidad total de elementos
# ni-1 / ni
# ni-2 / ni-1
# ni-3 / ni-2
# ni-4 / ni-3
# ni-5 / ni-4
aureo = fibonacci
for i in range(5):
    print(aureo[-2] / aureo[-1])
    aureo.pop()

# 10. A partir de la variable cadena ya dada, mostrar en qué posiciones
# aparece la letra "n"
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

for pos, char in enumerate(cadena):
    if char == "n":
        print(f"{char} aparece en la posicion No. {pos}")

# 11. Crear un diccionario e imprimir sus claves utilizando un iterador
dicc = {'Ciudad': ['Buenos Aires', 'Caracas', 'Bogotá', 'Lisboa', 'Roma'],
        'País': ['Argentina', 'Venezuela', 'Colombia', 'Portugal', 'Italia'],
        'Continente': ['América', 'América', 'América', 'Europa', 'Europa']}

for i in dicc:
    print(i)

# 12. Convertir en una lista la variable "cadena" del punto 10 y luego
# recorrerla con un iterador
cadenaLista = list(cadena)
for c in cadenaLista:
    print(c)

# 13. Crear dos listas y unirlas en una tupla utilizando la función zip
lis1 = ['run', 'fly', 'sleep']
lis2 = ['correr', 'volar', 'dormir']
lisZip = zip((lis1, lis2))
print(list(lisZip))

# 14. A partir de la siguiente lista de números, crear una nueva sólo si el
# número es divisible por 7
lis = [18, 21, 29, 32, 35, 42, 56, 60, 63, 71, 84, 90, 91, 100]
divisibleSeven = [i for i in lis if i % 7 == 0]
print(divisibleSeven)

# 15. A partir de la lista de a continuación, contar la cantidad total de
# elementos que contiene, teniendo en cuenta que un elemento de la lista
# podría ser otra lista:
diccLis = [[1, 2, 3, 4], 'rojo', 'verde', [
    True, False, False], ['uno', 'dos', 'tres']]
length = 0
for i in diccLis:
    if type(i) == list:
        for j in i:
            length += 1
    else:
        length += 1
print(length)

# 16. Tomar la lista del punto anterior y convertir cada elemento en una lista 
# si no lo es

for pos, obj in enumerate(diccLis):
    if type(obj) != list:
        diccLis[pos] = [obj]

print(diccLis)
