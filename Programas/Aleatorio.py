#modulo de programa
import random
#Se define la variable float y se le asigna valor
numero1=float(10.5)
#funcion es un conjunto de instrucciones
#la definicion forma una funcion
def miFuncion():
    #se convierte a float el numero aleatorio generado por}
    #random.randrange()(solo esta disponible si se importa un modulo random)
    numero2=float(random.randrange(1,10))
    #se utiliza meta sustitucion para mostrar resultados.
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))
#se ejecuta la funcion definida en el codigo
miFuncion()