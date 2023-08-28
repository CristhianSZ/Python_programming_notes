"""set es una serie de elementos que no se repiten
puede ser de tipo caracter o numerico """
def nombre(palabra):
    separado=set()
    for letra in palabra:
        separado.add(letra)
    mi_lista=list(separado)
    mi_lista.sort()
    return mi_lista
print(nombre("intercontinentalidad"))