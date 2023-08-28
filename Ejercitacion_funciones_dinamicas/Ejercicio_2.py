""" Ejercicio 2
Crea una funcion (suma_menores) que sume los numeros de una lista (almacenada en una variable lista_numeros)
siempre y cuando sean mayores a cero y menores a 1000 y devuelva el resultado de dicha suma
"""
lista_numeros=[]

op="si"
while (op=="si"):
    n= int(input("Ingrese un numero: "))
    lista_numeros.append(n)
    op=input("Desea agregar un numero al vector? (si/no)")

def suma_menores(lista_numeros):
    suma=0
    j=0
    for i in lista_numeros:
        if (i>=0) and (i<=1000):
            suma += lista_numeros[j]
            j += 1
        else:
            pass
    return suma

print(suma_menores(lista_numeros))