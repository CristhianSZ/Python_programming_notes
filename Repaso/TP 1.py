#Primer ejercicio
print("Primer ejercicio")
palabra = "ordenador"
print("El carácter que ocupa la quinta posición es:", palabra[5])

#Segundo ejercicio y tercero
print("Segundo y tercer ejercico")
oracion="En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son.";
print("El numero de caracteres es: ", len(oracion));
##En string.index(valuem start, end) no es necesario especificar la posicion de donde hasta donde buscar.
print("El índice de la primera aparición de la palabra práctica es: " ,oracion.index("práctica",0,76));
print("El índice de la ultima aparición de la palabra práctica es: " ,oracion.rindex("práctica",0,76));
"""
texto="Mis alumnos son muy buenos"
print("La cantidad de caracteres es: ",len(texto))
print("El caracter en la posicion es: ",texto[10])
print("El caracter esta en la posicion: ",texto.index("m",0,26))
print("El caracter esta en la posicion desde la ultima posicion es: ",texto.rindex("m",0,26))
"""
"""La manera que busca la profesora es:
texto=frase.index("practica")
print(texto)"""