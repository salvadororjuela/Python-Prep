# 1. Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
entero = 2
print(entero)
if entero < 0:
    print("Negativo")
elif entero > 0:
    print("Positivo")
else:
    print("El numero es 0")

# 2. Crear dos variables y un condicional que informe si son del mismo tipo de dato
par = 4
letra = "A"

if type(par) == type(letra):
    print("Los dos elementos son del mismo tipo")
else:
    print("Los elementos son de distinto tipo")

# 3. Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} es numero par")
    else:
        print(f"{i} impar")

# 4. En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for i in range(0, 6):
    alCubo = i ** 3
    print(f"{i} a la tercera potencia es igual a: {alCubo}")

# 5. Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
entero1 = int(input("Digite un numero entero mayor que 0: "))
for i in range(entero1):
    print(i)

# 6. Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
print("**********************************************************************")
numOriginal = entero1
if type(entero1) == int:
    if entero1 > 0:
        factorial = 1
        while entero1 > 0:
            factorial *= entero1
            entero1 -= 1
    else:
        print("El numero es menor que 0")
print(f"El factorial de {numOriginal} es {factorial}")
print("**********************************************************************")


# 7. Crear un ciclo for dentro de un ciclo while
cadena = "Pepalarepax"
while True:
    for letra in cadena:
        if letra != "x":
            print(letra)
        else:
            break
    break

# 8. Crear un ciclo while dentro de un ciclo for
ha = "Ha "
for i in range(1, 11):
    while True:
        print(ha * i)
        if i == 11:
            break
        break

# 9. Imprimir los números primos existentes entre 0 y 30
for i in range(2, 31):
    primo = True
    inicial = 2
    while inicial < i:
        if i % inicial == 0:
            primo = False
        inicial += 1

    if primo:
        print(f"El numero {i} es primo")

# 10. ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
for i in range(2, 31):
    primo = True
    inicial = 2
    while inicial < i:
        if i % inicial == 0:
            primo = False
            break
        inicial += 1

    if primo:
        print(f"El numero {i} es primo")

# 11. En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
sinBreak = 0
for i in range(2, 31):
    primo = True
    inicial = 2
    while inicial < i:
        sinBreak += 1
        if i % inicial == 0:
            primo = False
        inicial += 1

print(f"Los ciclos sin break fueron: {sinBreak} ciclos")

conBreak = 0
for i in range(2, 31):
    primo = True
    inicial = 2
    while inicial < i:
        conBreak += 1
        if i % inicial == 0:
            primo = False
            break
        inicial += 1

print(f"Ciclos con break: {conBreak} ciclos")
print(f"Se optimiza en un {(conBreak/sinBreak)*100}% cuando se usa el break")

# 12. Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
sinBreak = 0
for i in range(2, 50):
    primo = True
    inicial = 2
    while inicial < i:
        sinBreak += 1
        if i % inicial == 0:
            primo = False
        inicial += 1

print(f"Los ciclos sin break fueron: {sinBreak} ciclos")

conBreak = 0
for i in range(2, 50):
    primo = True
    inicial = 2
    while inicial < i:
        conBreak += 1
        if i % inicial == 0:
            primo = False
            break
        inicial += 1

print(f"Ciclos con break: {conBreak} ciclos")
print(f"Se optimiza en un {(conBreak/sinBreak)*100}% cuando se usa el break")

# 13. Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
arranque = 100
while arranque < 300:
    arranque += 1
    if arranque % 12 != 0:
        continue
    print(f"{arranque} es multiplo de 12")
    
# 14. Utilizar la función input() que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
while True:
    cantidad = input("Digite un numero mayor a 2: ")
    if cantidad == "fin":
        break
    cantidad = int(cantidad)
    if cantidad < 2:
        cantidad = input("Ingrese un numero mayor a 2: ")

    else:
        for i in range(2, cantidad):
            primo = True
            inicial = 2
            while inicial < i:
                if i % inicial == 0:
                    primo = False
                    break
                inicial += 1

            if primo:
                print(f"{i} es numero primo")


# 15. Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
primero = 100
ultimo = 300
while primero <= ultimo:
    if primero % 6 == 0:
        print(f"El numero es: {primero}")
        break
    primero += 1
