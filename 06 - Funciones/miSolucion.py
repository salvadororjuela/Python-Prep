# 1. Crear una función que reciba un número como parámetro y devuelva si True
# si es primo y False si no lo es
def primo(numero):
    esPrimo = True
    for i in range(2, numero):
        if numero % i == 0:
            esPrimo = False
            break
    return esPrimo


num = int(input("Digite un valor para verificar si es numero primo: "))

print(primo(num))


# 2. Utilizando la función del punto 1, realizar otra función que reciba de
# parámetro una lista de números y devuelva sólo aquellos que son primos en
# otra lista
numeros = [3, 11, 19, 45, 323, 1234, 50, 49, 7, 71]


def listaPrimos(numeros):
    primos = []
    for i in numeros:
        if primo(i):
            primos.append(i)
    return(primos)


print(listaPrimos(numeros))


# 3. Crear una función que al recibir una lista de números, devuelva el que
# más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que
# devuelva cualquiera
def repetidos(lis):
    lis.sort()
    maximo = 0
    temp = 0
    num = 0
    for i in lis:
        maximo = lis.count(i)
        if maximo > temp:
            temp = maximo
            num = i
    return f"""el numero que mas se repite es: {num} y se repite: {maximo} veces"""


lis = [1, 1, 22, 5, 6, 8, 10, 22, 22, 22, 5, 6, 4, 11, 9, 5]
print(repetidos(lis))


# 4. A la función del punto 3, agregar un parámetro más, que permita elegir si
# se requiere el menor o el mayor de los mas repetidos.
def modal(lista2, orden=True):
    masRepetido = []
    cantidad = []

    if orden:
        lista2.sort()
    else:
        lista2.sort(reverse=True)

    for i in lista2:
        if i in masRepetido:
            j = masRepetido.index(i)
            cantidad[j] += 1
        else:
            masRepetido.append(i)
            cantidad.append(1)

    num = masRepetido[0]
    maximo = cantidad[0]

    for indice, elemento in enumerate(masRepetido):
        if cantidad[indice] > maximo:
            maximo = cantidad[indice]
            num = masRepetido[indice]

    return f"""el numero que mas se repite es: {num} y se repite: {maximo} veces"""


lista2 = [22, 1, 1, 22, 5, 6, 8, 10, 22, 22, 5, 6, 5, 4, 11, 9, 5]
orden = input("Indique 'True' para el mayor o 'False' para el menor modal: ")
print(modal(lista2, orden))


# 5. Crear una función que convierta entre grados Celsius, Farenheit y Kelvin
# Fórmula 1: (°C × 9/5) + 32 = °F
# Fórmula 2: °C + 273.15 = °K
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de
# destino
def temperatura(valor, origen, destino):
    nuevaTemperatura = 0

    if origen == "C" and destino == "F":
        nuevaTemperatura = float(valor) * (9/5) + 32

    if origen == "C" and destino == "K":
        nuevaTemperatura = float(valor) + 273.15

    if origen == "F" and destino == "C":
        nuevaTemperatura = (float(valor) - 32) * (5/9)

    if origen == "F" and destino == "K":
        nuevaTemperatura = (float(valor) + 459.67) * (5/9)

    if origen == "K" and destino == "C":
        nuevaTemperatura = float(valor) - 273.15

    if origen == "K" and destino == "F":
        nuevaTemperatura = (float(valor) - 273.15) * (9/5) + 32

    if origen == "C" and destino == "C":
        nuevaTemperatura = valor

    if origen == "F" and destino == "F":
        nuevaTemperatura = valor

    if origen == "K" and destino == "K":
        nuevaTemperatura = valor

    return f"{valor}  º{origen} equivalen a {nuevaTemperatura} º{destino}"


valor = ""
origen = ""
destino = ""

while True:
    valor = input("introduzca el valor numerico a convertir: ")
    if valor.isnumeric():
        valor = int(valor)
        break

while True:
    origen = input("Introduzca el tipo de temperatura de entrada: 'C', 'F', 'K': ")
    origen = origen.upper()
    if origen == "C" or origen == "F" or origen == "K":
        break

while True:
    destino = input("Introduzca el tipo de salida de temperatura : 'C', 'F', 'K': ")
    destino = destino.upper()
    if destino == "C" or destino == "F" or destino == "K":
        break

print(temperatura(valor, origen, destino))

# 6. Iterando una lista con los tres valores posibles de temperatura que
# recibe la función del punto 5, hacer un print para cada combinación de los
# mismos:
metricas = ["C", "F", "K"]
for i in range(0, 3):
    for j in range(0, 3):
        print(temperatura(1, metricas[i], metricas[j]))


# 7. Armar una función que devuelva el factorial de un número. Tener en cuenta
# que el usuario puede equivocarse y enviar de parámetro un número no entero o
# negativo

def factorial(numero):
    if numero > 1:
        numero = numero * factorial(numero - 1)
    return numero


number = ""

while True:
    number = input("Numero para factorial: ")

    if number.isnumeric():
        number = int(number)
        if number < 0:
            print("El numero debe ser mayor a 0")
    else:
        continue
    break

print(factorial(5))
