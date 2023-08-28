def sumamenores(lista_numeros):
    suma=0
    for numero in lista_numeros:
        if (0<numero) and (numero<1000):
            suma+=numero
        return suma
entrada = input ("Ingrese los numeros separados por un espacio")
"""split sirve para ingresar datos a un vector con espacios es algo similar a .append()"""
numeros=[int(num) for num in entrada.split()]
resultado = sumamenores((numeros))
print("La suma de los menores a 1000 es : ",resultado)