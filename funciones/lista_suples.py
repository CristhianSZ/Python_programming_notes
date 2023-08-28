"""
Diccionario o suples: esta comprendido por dos elementos
"""
lista=[("a",1),("b",2),("c",3)]
"""Si yo quiero recorrerlo y si quiero que especifica
si solo agrego un recorredor i recorrer solo 1 le agrego otro recorredor"""
for i,x in lista:
    print(i)
    print(x)
"""Realizar una lista de tipos de cafe con sus precios y mostrar por pantalla solo los cafes 

Mostrar el mayor precio de la lista de cafe"""


listacafe=[("Cafe Arabica",2),("Cafe Robusta",4),("Expreso",6),("Ristretto",8)]
for cafe,precio in listacafe:
    print(cafe)