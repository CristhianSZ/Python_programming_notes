"""1) Crea una funcion (todos_positivos) que resiva una lista de numeros
como parametro y devuelva True si todos los valores de una lista son positivos
y False si almenos 1 de los valores es negativo"""
numeros=[]
op="si"
while (op=="si"):
    n= int(input("Ingrese un numero: "))
    numeros.append(n)
    op=input("Desea agregar un numero al vector? (si/no)")
def todos_positivos(numeros):
    for i in numeros:
        if (i<0):
            return False
    return True

print(todos_positivos(numeros))

