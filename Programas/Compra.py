numero1=input("Numero 1:")
numero2=input("Numero 2:")
salida="Numeros proporcionados: {} y {}. {}."
if (numero1==numero2):
    #entra aqui si los numeros capturados son iguales.
    print(salida.format(numero1, numero2,"Los numeros son iguales"))
else:
    #condicionales unidades, if dentro de otro if
    #si los numeros iguales
    if numero1>numero2:
        #Reporta si el primer numero es mayor al segundo
        print(salida.format(numero1,numero2,"El mayor es el primero"))
    else:
        #o de lo contarario, si el primero no es mayor al segundo.
        print(salida.format(numero1, numero2,"El mayor es el segundo"))
