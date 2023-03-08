""" 1. Con la clase creada en el módulo 7, tener en cuenta diferentes casos en
que el código pudiera arrojar error. Por ejemplo, en la creación del objeto
recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo
de dato?"""
import importlib
import miModuloCap7 as mod

# h = mod.Herramientas([1, 2, 3, 4, 1, 2, 3, 1, 2, 1])

# h([1, 2, 3, 4, 1, 2, 3, 1, 2, 1])


# Para recargar cambios hechos en modulos externos que pueden no verse
# reflejados a menos que se hiciera el proceso de borrar las variables
# de la memoria y recargar modulo que usa programa.

# import importlib
# importlib.reload(h)


""" 2. En la función que hace la conversión de grados, validar que los
parámetros enviados sean los esperados, de no serlo, informar cuáles son los
valores esperados."""
# Para solucionar esto se puede hacer que en el programa haya un print
# que reporta esta informacion

""" 3. Importar el modulo "unittest" y crear los siguientes casos de pruebas
sobre la clase utilizada en el punto 2
Creacion del objeto incorrecta
Creacion correcta del objeto
Metodo valor_modal()
Se puede usar "raise ValueError()" en la creación de la clase para verificar
el error. Investigar sobre esta funcionalidad."""
import unittest

class testGrados(unittest.TestCase):
    def objetoIncorrecto(self):
        param = "hola"
        self.assertRaises(ValueError, mod.Herramientas, param)
        
    def objetoCorrecto(self):
        listaEvaluar = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
        h1 = mod.Herramientas(listaEvaluar)
        self.assertEqual(h1.lista, listaEvaluar) 
        
    def testModal(self):
        list = [1, 2, 1, 3]
        h1 = mod.Herramientas(list)
        moda, veces = h1.modales()
        moda = [moda]
        moda.append(veces)
        resultado = [1, 2]
        self.assertEqual(moda, resultado)


importlib.reload(mod)
unittest.main(argv=[''], verbosity=2, exit=False)
    

""" 4. Probar una creación incorrecta y visualizar la salida del 'raise'"""
h2 = mod.Herramientas("Alguna Cosa")

""" 5. Agregar casos de pruebas para el método verifica_primos() realizando el
cambio en la clase, para que devuelva una lista de True o False en función
de que el elemento en la posisicón sea o no primo"""
class testPrimos(unittest.TestCase):
    
    def pruebaPrimos(self):
        lista = [3, 5, 10, 11]
        h1 = mod.Herramientas(lista)
        valor = h1.primos(valor)
        primosEsperados = [True, True, False, True]
        self.assertEqual(valor, primosEsperados)


unittest.main(argv=[''], verbosity=2, exit=False)

""" 6. Agregar casos de pruebas para el método conversion_grados()"""

""" 7. Agregar casos de pruebas para el método factorial()"""

""" 8. Completar el código en las funciones del archivo "checkpoint.py" y
probarlo a partir de la ejecución del script 'tests.py'"""
