#se declaran las variables
acomulado=int(0)
numero=str("")
while True:
    numero=input("Dame un numero entero: ")
    if numero=="":
        #Si el numero es vacio sale.
        print("vacio.Salida del programa")
        break
    else:
        #Si se proporciona valor, acomulado = acomulado + numero
        #se realiza el calculo usando suma incluyendo(+=)
        salida="Monto acomulado: {}"
        print(salida.format(acomulado))