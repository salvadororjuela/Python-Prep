class Herramientas:
    def __init__(self, lista):
        if (type(lista) != list):
            self.lista = [0]
            raise ValueError('Se ha creado con un elemento 0. Se esperaba una lista de núemeros enteros')
        else:
            self.lista = lista

    # Calcula los numeros primos de la lista
    def primos(self):
        for i in self.lista:
            self.primo(i)

    def primo(self, numero):
        esPrimo = True
        for i in range(2, numero):
            if numero % i == 0:
                esPrimo = False
                return esPrimo

        if esPrimo:
            print(f"{numero} SI ES PRIMO")
        else:
            print(f"{numero} no es primo")

    # Calcula el modal de la lista y su frecuencia
    def modales(self):
        masRepetido = []
        cantidad = []

        for i in self.lista:
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

        return [num, maximo]

    # convierte las temperaturas de la lista de grados centigrados a fahrenheit
    def temperaturas(self):
        for i in self.lista:
            self.temperatura(i)

    def temperatura(self, valor, origen="C", destino="F"):

        nuevaTemperatura = float(valor) * (9/5) + 32

        print(f"{valor}  º{origen} equivalen a {nuevaTemperatura} º{destino}")
