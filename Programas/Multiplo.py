#Se captura un numero y se almacena cuando se convierta en int
numero=int(input("Dame un numero entero: "))
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)
if((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("correcto.")
else:
    print("incorrecto.")