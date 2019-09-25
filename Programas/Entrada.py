entrada=input()
print(type(entrada))
#la variable boolanea contiene el resultado de verificar
#si la captura es dijito y no se encuentra en un punto
#en lo capturado lo que indicaria que trata de un numero decimal
#es decir float si  si find retonda -1
#quiere decir en este caso en un punto decimal
#no se encontro si es entero es true#lo capturado es entero
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):
    #linea que se ejecutara si la condicion es verdadera(true)
    print("Dato entero. ¡Muy bien!")
else:
    #Linea que se ejecutara si la condicion es falsa(false)
    print("Dato no entero. Intente de nuevo.")
