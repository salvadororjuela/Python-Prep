import math
# 1. Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
entero = 1024
print(entero)
# 2. Imprimir el tipo de dato de la constante 8.5
print(type(8.5))
# 3. Imprimir el tipo de dato de la variable creada en el punto 1
print(type(entero))
# 4. Crear una variable que contenga tu nombre
nombre = "Salvador"
# 5. Crear una variable que contenga un número complejo
complejo = 1 + 1j
# 6. Mostrar el tipo de dato de la variable crada en el punto 5
print(type(complejo))
# 7. Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pinumber = round(math.pi, 4)
# 8. Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
verdad = True
falso = False
# 9. Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print(type(verdad))
print(type(falso))
# 10. Asignar a una variable, la suma de un número entero y otro decimal
decimas = .89
sumatoria = entero + decimas
# 11. Realizar una operación de suma de números complejos
sumaComplejo = complejo + 2j
# 12. Realizar una operación de suma de un número real y otro complejo
sumaRealComplejo = 8.5 + sumaComplejo
print(sumaRealComplejo)
# 13. Realizar una operación de multiplicación
print(entero * decimas)
# 14. Mostrar el resultado de elevar 2 a la octava potencia
print(2 ** 8)
# 15. Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
cociente = 27 / 4
print(cociente)
# 16. De la división anterior solamente mostrar la parte entera
divExacta = 27 // 4
print(divExacta)
# 17. De la división de 27 entre 4 mostrar solamente el resto
resto = 27 % 4
print(resto)
# 18. Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print((4 * divExacta) + resto)
# 19. Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
apellido = " Orjuela"
print(nombre + apellido)
# 20. Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print("2" == 2) # Es falso porque el primer dos es un caracter y el segundo es un entero, son dos datos diferentes
# 21. Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(int("2") == 2)
# 22. ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# R//: El error es porque no se puede convertir a float un numero que separa sus decimales con comas. Debe ser punto el caracter que separa.

# 23. Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
tres = 3
tres -= 1
print(tres)
# Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
operacionBinaria = 1 << 2
print(operacionBinaria)
# Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
# No es valido porque no se pueden concatenar un dato tipo entero con uno tipo string

# Realizar una operación válida entre valores de tipo entero y string
cadena = "Ha "
entero1 = 5
operacionValida = entero1 * cadena
print(operacionValida)
