#Declaro variable
numero="1234"
#Se mostrara la salida de type
print(type(numero))
#Se convierte a int
numero=int(numero)
#Se muestra como cambia aun que sea la misma variable
print(type(numero))
#Se declara un str para hacer la sustitucion
#Valores proporcioados usando format
salida="El número utilizado es {}"
#se muestra resultado
#se coloca el valor de numero{}.
print(salida.format(numero))