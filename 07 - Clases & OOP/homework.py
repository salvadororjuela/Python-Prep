import miModulo


# 1. Crear la clase vehículo que contenga los atributos:
# Color
# Si es moto, auto, camioneta ó camión
# Cilindrada del motor


# 2. A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:
# Acelerar
# Frenar
# Doblar

# 4. Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a
# que velocidad se encuentra y su dirección. Y otro método que muestre color,
# tipo y cilindrada

class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0

    def acelerar(self, vel):
        self.velocidad += vel

    def frenar(self, vel):
        self.velocidad -= vel
        print(f"El vehiculo desacelero {self.velocidad} km/h")

    def doblar(self, giro):
        self.direccion += giro
        
    def estado(self):
        print(f"la velocidad es {self.velocidad} y giro {self.direccion} grados")
    
    def datosVehiculo(self):
        print(f"El vehiculo es un {self.tipo}, de color {self.color} y su cilindrada es {self.cilindrada}cc")


# 3. Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar
# luego el resultado
renault = Vehiculo("Rojo", "Carro", 1600)
honda = Vehiculo("Azul", "Moto", 200)
enduro = Vehiculo("Verde", "Bote", 800)

renault.doblar(30)
honda.acelerar(100)
honda.doblar(15)
enduro.frenar(50)

renault.datosVehiculo()
honda.estado()

# 5. Crear una clase que permita utilizar las funciones creadas en la práctica
# del módulo 6
# Verificar Primo
# Valor modal
# Conversión grados
# Factorial


class funciones:
    def __init__(self) ->None:
        pass

    def primo(self, numero):
        esPrimo = True
        for i in range(2, numero):
            if numero % i == 0:
                esPrimo = False
                break

        if esPrimo:
            print(f"{numero} SI ES PRIMO")
        else:
            print(f"{numero} no es primo")

    def modal(self, lista2, orden=True):
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

        return f"el numero que mas se repite es: {num} y se repite: {maximo} veces"

    def temperatura(self, valor, origen, destino):
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

    def factorial(self, number):
        if number > 1:
            # Para hacer recursion, la funcion debe llamarse como un metodo de
            # self (self.factorial(number - 1))
            number = number * self.factorial(number - 1)
        return number


# 6. Probar las funciones incorporadas en la clase del punto 5
# Verificar primo
numPrimo = funciones()
numPrimo.primo(11)

# Valor modal
lista2 = [22, 1, 1, 22, 5, 6, 8, 10, 22, 22, 5, 6, 5, 4, 11, 9, 5]
orden = input("Indique 'T' para el mayor o 'F' para el menor modal: ")
modal = funciones()

print((modal.modal(lista2, orden)))

# Conversión grados
valor = ""
origen = ""
destino = ""

while True:
    valor = input("introduzca el valor numerico a convertir: ")
    if valor.isnumeric():
        valor = int(valor)
        break

while True:
    origen = input(
        "Introduzca el tipo de temperatura de entrada: 'C', 'F', 'K': ")
    origen = origen.upper()
    if origen == "C" or origen == "F" or origen == "K":
        break

while True:
    destino = input(
        "Introduzca el tipo de salida de temperatura : 'C', 'F', 'K': ")
    destino = destino.upper()
    if destino == "C" or destino == "F" or destino == "K":
        break

cambioTemperatura = funciones()
print(cambioTemperatura.temperatura(valor, origen, destino))

# Factorial
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

factor = funciones()
print(factor.factorial(number))


# 7. Es necesario que la clase creada en el punto 5 contenga una lista, sobre
# la cual se aplquen las funciones incorporadas
# class Herramientas:
#     def __init__(self, lista):
#         self.lista = lista

#     # Calcula los numeros primos de la lista
#     def primos(self):
#         for i in self.lista:
#             self.primo(i)

#     def primo(self, numero):
#         esPrimo = True
#         for i in range(2, numero):
#             if numero % i == 0:
#                 esPrimo = False
#                 break

#         if esPrimo:
#             print(f"{numero} SI ES PRIMO")
#         else:
#             print(f"{numero} no es primo")

#     # Calcula el modal de la lista y su frecuencia
#     def modales(self):
#         masRepetido = []
#         cantidad = []

#         for i in self.lista:
#             if i in masRepetido:
#                 j = masRepetido.index(i)
#                 cantidad[j] += 1
#             else:
#                 masRepetido.append(i)
#                 cantidad.append(1)

#         num = masRepetido[0]
#         maximo = cantidad[0]

#         for indice, elemento in enumerate(masRepetido):
#             if cantidad[indice] > maximo:
#                 maximo = cantidad[indice]
#                 num = masRepetido[indice]

#         return f"el numero que mas se repite es: {num} y se repite: {maximo} veces"

#     # convierte las temperaturas de la lista de grados centigrados a fahrenheit
#     def temperaturas(self):
#         for i in self.lista:
#             self.temperatura(i)

#     def temperatura(self, valor, origen="C", destino="F"):

#         nuevaTemperatura = float(valor) * (9/5) + 32

#         print(f"{valor}  º{origen} equivalen a {nuevaTemperatura} º{destino}")

    # def factorial(self, number):
    #     if number > 1:
    #         # Para hacer recursion, la funcion debe llamarse como un metodo de
    #         # self (self.factorial(number - 1))
    #         number = number * self.factorial(number - 1)
    #     return number


lista = [1, 1, 2, 5, 8, 8, 9, 11, 15, 16, 16, 16, 18, 20]
# primos()
numerosVarios = miModulo.Herramientas(lista)
numerosVarios.primos()

# modales()
print(numerosVarios.modales())

# temperaturas()
numerosVarios.temperaturas()

# 8. Crear un archivo .py aparte y ubicar allí la clase generada en el punto
# anterior. Luego realizar la importación del módulo y probar alguna de sus
# funciones EL ARCHIVO SE IMPORTA EN EL ENCABEZADO DEL PRESENTE PROGRAMA
