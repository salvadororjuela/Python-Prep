# 2) Crear un script con el nombre "clase09_ej2.py2" que reciba como un valor de
# temperatura en grados centígrados, un valor de humedad y por último si llovio(Con
# True o False). Y que cada vez que sea invocado, cargue en el archivo provisto
# "clase09_ej2.csv" una marca de tiempo y esa información.

# Para trabajar con tipos de datos relacionados con la medición del tiempo, como ser
# fechas, horarios o marcas de tiempo se puede utilizar la clase * datetime *

import datetime, sys

if sys.argv == 4:
    
    x = datetime.datetime.now()
    x = datetime.datetime.timestamp(x)

    archivoClima = open("clase09_ej2.csv", "a")

    archivoClima.write(f"Timestamp: {x} | Temperatura: {sys.argv[1]} | Humedad: {sys.argv[2]} | Llovio: {sys.argv[3]} \n")
    
    archivoClima.close()

else:
    print("Se intrudujeros menos o mas de 3 argumentos")