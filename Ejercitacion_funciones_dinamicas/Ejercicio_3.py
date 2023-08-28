"""Ejercicio 3
Crea una funcion (cantidad_pares) que cuente la cantidad de numeros pares que existe en una lista (lista_numeros)
y devuelva el resultado de dicha cuenta """

lista_numeros=[]

op="si"
while (op=="si"):
    n= int(input("Ingrese un numero: "))
    lista_numeros.append(n)
    op=input("Desea agregar un numero al vector? (si/no)")

def cantidad_pares(lista_numeros):
    cant_pares = 0
    for i in lista_numeros:
        if (i%2==0):
            cant_pares+=1
        else:
            pass
    return cant_pares
print("La cantidad de numeros pares es la siguiente: ")
print(cantidad_pares(lista_numeros))

