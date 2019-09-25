for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    #print sin argumento en un salto de linea
    print()
    #dentro de un for, se pone otro for
    for j in range(1,11):
        #aqui i contiene el numero base de la tabla
        #y j el elemento de la tabla
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        #al concluir con las iteraciones indicadas
        #se ejecuta el codigo que es un salto de lienea
        print()